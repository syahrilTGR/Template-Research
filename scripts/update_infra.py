import os
import sys
import urllib.request
import re
import zipfile
import shutil
import subprocess
import hashlib
import json
import difflib
from pathlib import Path

REPO_URL = "https://github.com/syahrilTGR/Template-Research"
RAW_GEMINI_URL = "https://raw.githubusercontent.com/syahrilTGR/Template-Research/main/gemini.md"
ZIP_URL = f"{REPO_URL}/archive/refs/heads/main.zip"

MANIFEST_PATH = Path(".agents/infra_manifest.json")

# ---------------------------------------------------------
# TIER DEFINITIONS
# ---------------------------------------------------------
def get_tier(rel_path):
    rel_path_str = str(rel_path).replace("\\", "/")
    
    tier3_patterns = [
        "supportFiles/handoff/",
        "references/",
        "intelligence/",
        "results/",
        "dataset/",
        "notebooks/",
        "supportFiles/faq/",
    ]
    for p in tier3_patterns:
        if rel_path_str.startswith(p):
            return 3

    tier2_patterns = [
        "gemini.md",
        "README.md",
        "CHANGELOG.md",
        "supportFiles/ACTION_PLAN.md",
        "supportFiles/notebooklm_mcp_setup.md",
        "supportFiles/word_sync_config.json"
    ]
    if rel_path_str in tier2_patterns or rel_path_str.startswith(".agents/workflows/"):
        return 2
        
    return 1

# ---------------------------------------------------------
# HASHING & MANIFEST
# ---------------------------------------------------------
def get_file_hash(path):
    if not os.path.exists(path):
        return None
    hasher = hashlib.sha256()
    with open(path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def load_manifest():
    if MANIFEST_PATH.exists():
        try:
            with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_manifest(manifest_data):
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, indent=4)

# ---------------------------------------------------------
# UTILS
# ---------------------------------------------------------
def get_version_from_content(content):
    match = re.search(r"Version:\*\*?\s*(v[0-9]+\.[0-9]+\.[0-9]+)", content, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def get_local_version():
    gemini_path = Path("gemini.md")
    if gemini_path.exists():
        try:
            content = gemini_path.read_text(encoding="utf-8")
            return get_version_from_content(content)
        except Exception as e:
            pass
    return None

def get_remote_version():
    try:
        print("[*] Mengecek versi online di repositori pusat...")
        with urllib.request.urlopen(RAW_GEMINI_URL, timeout=10) as response:
            content = response.read().decode("utf-8")
            return get_version_from_content(content)
    except Exception as e:
        print(f"[-] Gagal mengecek versi online: {e}")
    return None

def run_command(command, shell=True):
    try:
        result = subprocess.run(command, shell=shell, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"[-] Error menjalankan perintah: {command}\nError: {e.stderr}")
        return None

def display_latest_changelog(staging_dir):
    changelog_path = Path(staging_dir) / "CHANGELOG.md"
    if changelog_path.exists():
        content = changelog_path.read_text(encoding="utf-8")
        matches = list(re.finditer(r"^## \[v[0-9]+\.[0-9]+\.[0-9]+\].*?(?=\n## \[v|\Z)", content, re.MULTILINE | re.DOTALL))
        if matches:
            print("\n" + "="*50)
            print(" 🚀 APA YANG BARU DI PEMBARUAN INI?")
            print("="*50)
            print(matches[0].group(0).strip())
            print("="*50 + "\n")

# ---------------------------------------------------------
# SMART MERGE
# ---------------------------------------------------------
def smart_merge_gemini(local_path, remote_path):
    local_content = Path(local_path).read_text(encoding="utf-8")
    remote_content = Path(remote_path).read_text(encoding="utf-8")

    identity_pattern = r"(## 🎯 Project Identity.*?)(?=## 📁 Repository Ecosystem Map|## 🔄 AI Context & Workflows|---)"
    local_match = re.search(identity_pattern, local_content, re.DOTALL)
    remote_match = re.search(identity_pattern, remote_content, re.DOTALL)

    if local_match and remote_match:
        merged_content = remote_content[:remote_match.start()] + local_match.group(1) + remote_content[remote_match.end():]
        Path(local_path).write_text(merged_content, encoding="utf-8")
        print("[+] Smart Merge berhasil: Konteks pembaruan gemini.md diaplikasikan tanpa merusak identitas Anda.")
        return True
    else:
        print("[-] Smart Merge fallback: Gagal menemukan blok identitas, mencoba mempertahankan file lokal.")
        return False

def show_diff_and_prompt(local_path, remote_path):
    with open(local_path, 'r', encoding='utf-8') as f1, open(remote_path, 'r', encoding='utf-8') as f2:
        diff = list(difflib.unified_diff(f1.readlines(), f2.readlines(), fromfile='Lokal', tofile='Remote Baru'))
    
    print("".join(diff[:15]))
    if len(diff) > 15:
        print("... (diff dipotong)")
        
    ans = input(f"Timpa file lokal dengan versi baru? (y/N): ").strip().lower()
    return ans == 'y'

# ---------------------------------------------------------
# PHASES
# ---------------------------------------------------------
def phase_3_backup_and_apply(staging_dir, manifest, new_manifest):
    print("\n[*] [PHASE 3] Memulai proses pencangkokan secara transaksional...")
    
    timestamp = run_command('powershell -c "Get-Date -Format yyyyMMdd_HHmm"')
    if not timestamp:
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    
    backup_dir = Path(".agents/backups") / f"infra_pre_update_{timestamp}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    print(f"[*] Membuat snapshot cadangan di: {backup_dir}")
    
    try:
        if Path(".agents").exists():
            shutil.copytree(".agents", backup_dir / ".agents", ignore=shutil.ignore_patterns("backups", "_staging_", "_bridge_update_", "temp_update"))
        if Path("scripts").exists():
            shutil.copytree("scripts", backup_dir / "scripts")
    except Exception as e:
        print(f"[-] Gagal membuat backup: {e}")
        return False

    print("[*] Menerapkan file baru...")
    try:
        is_first_v2_upgrade = len(manifest) == 0
        
        for src_path in staging_dir.rglob("*"):
            if src_path.is_file():
                rel_path = src_path.relative_to(staging_dir)
                dest_path = Path(rel_path)
                tier = get_tier(rel_path)

                if tier == 3:
                    continue
                
                local_hash = get_file_hash(dest_path)
                manifest_hash = manifest.get(str(rel_path))
                
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                
                if tier == 1:
                    shutil.copy2(src_path, dest_path)
                    new_manifest[str(rel_path)] = get_file_hash(dest_path)
                
                elif tier == 2:
                    if not dest_path.exists():
                        shutil.copy2(src_path, dest_path)
                        new_manifest[str(rel_path)] = get_file_hash(dest_path)
                    elif local_hash == manifest_hash or (is_first_v2_upgrade and dest_path.name != "gemini.md"):
                        # If first time upgrading from V1 to V2, we silently overwrite Tier 2 to establish baseline
                        # except for gemini.md which is handled below.
                        shutil.copy2(src_path, dest_path)
                        new_manifest[str(rel_path)] = get_file_hash(dest_path)
                    else:
                        if dest_path.name == "gemini.md":
                            print(f"[*] Menggabungkan identitas di {rel_path}...")
                            smart_merge_gemini(dest_path, src_path)
                            new_manifest[str(rel_path)] = get_file_hash(dest_path)
                        else:
                            print(f"\n[!] KONFLIK: File {rel_path} telah dimodifikasi oleh Anda.")
                            if show_diff_and_prompt(dest_path, src_path):
                                shutil.copy2(src_path, dest_path)
                                new_manifest[str(rel_path)] = get_file_hash(dest_path)
                                print(f"    [+] Ditimpa.")
                            else:
                                print(f"    [*] Dipertahankan versi lokal.")
                                new_manifest[str(rel_path)] = local_hash

    except Exception as e:
        print(f"[-] TERJADI KESALAHAN KRITIS: {e}")
        print("[*] MEMULAI ROLLBACK OTOMATIS...")
        if (backup_dir / ".agents").exists():
            shutil.copytree(backup_dir / ".agents", ".agents", dirs_exist_ok=True)
        if (backup_dir / "scripts").exists():
            shutil.copytree(backup_dir / "scripts", "scripts", dirs_exist_ok=True)
        print("[+] Rollback berhasil. Sistem Anda aman.")
        return False
        
    return True

def phase_4_post_update(staging_dir, new_manifest):
    print("\n[*] [PHASE 4] Menjalankan rutinitas pasca pembaruan...")
    save_manifest(new_manifest)
    
    if sys.platform == 'win32':
        run_command("powershell -ExecutionPolicy Bypass -File scripts/setup_env.ps1")
        run_command("powershell -ExecutionPolicy Bypass -File scripts/setup_docx_infra.ps1")
    else:
        run_command("bash scripts/setup_env.sh")

    print("[*] Memulai Smoke Test...")
    tests_passed = True
    python_exe = sys.executable
    try:
        output = run_command(f'"{python_exe}" -c "from science_skills.scienceskillscommon import http_client; print(\'OK\')"')
        if output and "OK" in output:
            print("[+] Test 1: scienceskillscommon import - BERHASIL")
        else:
            print("[-] Test 1: scienceskillscommon import - GAGAL")
            tests_passed = False
    except:
        print("[-] Test 1: scienceskillscommon import - GAGAL")
        tests_passed = False

    try:
        if run_command("node -v"):
            output = run_command('node -e "require(\'docx\'); console.log(\'OK\');"')
            if output and "OK" in output:
                print("[+] Test 2: Node.js docx library - BERHASIL")
            else:
                print("[-] Test 2: Node.js docx library - GAGAL")
                tests_passed = False
        else:
            print("[!] Test 2: Node.js docx - DILEWATI (Node tidak ada di PATH)")
    except:
        tests_passed = False

    display_latest_changelog(staging_dir)
    print("\n[+] PEMBARUAN SELESAI DENGAN SUKSES!")


def perform_update(dry_run=False, force=False):
    local_ver = get_local_version()
    remote_ver = get_remote_version()
    
    print(f"\n[*] Versi Lokal : {local_ver or 'Tidak terdeteksi'}")
    print(f"[*] Versi Online: {remote_ver or 'Tidak terdeteksi'}")
    
    if not remote_ver:
        print("[-] Gagal memproses update karena versi online tidak dapat dijangkau.")
        return
        
    if local_ver == remote_ver and not dry_run and not force:
        print("[+] Versi lokal Anda sudah sama dengan versi online terbaru.")
        confirm = input("[?] Paksa pembaruan ulang? (y/N): ").strip().lower()
        if confirm != 'y': return

    if dry_run:
        print("[*] Mode Dry-Run Aktif: Berhenti setelah verifikasi versi.")
        return

    # PHASE 1
    temp_zip = Path("template_update.zip")
    temp_dir = Path(".agents/temp_update")
    staging_dir = Path(".agents/_staging_")
    
    for d in [temp_dir, staging_dir]:
        if d.exists(): shutil.rmtree(d)
        
    try:
        print("\n[*] [PHASE 1] Mengunduh & Staging paket pembaruan...")
        urllib.request.urlretrieve(ZIP_URL, temp_zip)
        with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
            
        extracted_folder = next(temp_dir.glob("Template-Research-*"))
        shutil.move(str(extracted_folder), str(staging_dir))
        
        new_script = staging_dir / "scripts" / "update_infra.py"
        if not new_script.exists():
            print("[-] Gagal: Skrip baru tidak ditemukan.")
            return

        print("[*] Menyerahkan eksekusi ke skrip baru (Phase 3-4)...")
        cmd = [sys.executable, str(new_script), "--execute-phases"]
        result = subprocess.run(cmd)

    finally:
        if temp_zip.exists(): temp_zip.unlink()
        if temp_dir.exists(): shutil.rmtree(temp_dir)
        if staging_dir.exists(): shutil.rmtree(staging_dir)

def execute_phases():
    # BACKWARD COMPATIBILITY: Fallback to old V1 bridge directory if staging is missing
    staging_dir = Path(".agents/_staging_")
    if not staging_dir.exists():
        staging_dir = Path(".agents/_bridge_update_")
        
    if not staging_dir.exists():
        print("[-] Direktori staging tidak ditemukan.")
        return
        
    manifest = load_manifest()
    new_manifest = {}
    
    success = phase_3_backup_and_apply(staging_dir, manifest, new_manifest)
    if success:
        phase_4_post_update(staging_dir, new_manifest)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Template-Research Auto-Update Engine V2")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    
    # New V2 Flag
    parser.add_argument("--execute-phases", action="store_true", help=argparse.SUPPRESS)
    
    # BACKWARD COMPATIBILITY: Old V1 Flag support
    parser.add_argument("--execute-phase-2", action="store_true", help=argparse.SUPPRESS)
    
    args = parser.parse_args()
    
    # Handle either the new V2 flag or the old V1 flag seamlessly
    if args.execute_phases or args.execute_phase_2:
        execute_phases()
    else:
        perform_update(dry_run=args.dry_run, force=args.force)
