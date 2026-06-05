import os
import sys
import urllib.request
import re
import zipfile
import shutil
import subprocess
from pathlib import Path

REPO_URL = "https://github.com/syahrilTGR/Template-Research"
RAW_GEMINI_URL = "https://raw.githubusercontent.com/syahrilTGR/Template-Research/main/gemini.md"
ZIP_URL = f"{REPO_URL}/archive/refs/heads/main.zip"

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
            print(f"[-] Gagal membaca gemini.md lokal: {e}")
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

def create_backup():
    timestamp = run_command('powershell -c "Get-Date -Format yyyyMMdd_HHmm"')
    if not timestamp:
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    
    backup_dir = Path(".agents/backups") / f"infra_pre_update_{timestamp}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    print(f"[*] Membuat cadangan infrastruktur lokal di: {backup_dir}")
    
    # Backup .agents
    agents_dest = backup_dir / ".agents"
    shutil.copytree(".agents", agents_dest, ignore=shutil.ignore_patterns("backups", "_bridge_update_", "temp_update"))
    
    # Backup scripts
    scripts_dest = backup_dir / "scripts"
    shutil.copytree("scripts", scripts_dest)
    
    print("[+] Cadangan berhasil dibuat.")
    return backup_dir

def run_post_update_setups():
    print("[*] Menjalankan skrip auto-konfigurasi pasca pembaruan...")
    if sys.platform == 'win32':
        run_command("powershell -ExecutionPolicy Bypass -File scripts/setup_env.ps1")
        run_command("powershell -ExecutionPolicy Bypass -File scripts/setup_docx_infra.ps1")
    else:
        run_command("bash scripts/setup_env.sh")

def run_smoke_test():
    print("[*] Memulai Smoke Test pasca pembaruan...")
    tests_passed = True
    
    # Test 1: Verify scienceskillscommon import
    try:
        # Run python check to see if package is importable
        # Determine the local python path (e.g. from venv)
        python_exe = sys.executable
        test_code = "from science_skills.scienceskillscommon import http_client; print('HTTP Client import OK')"
        output = run_command(f'"{python_exe}" -c "{test_code}"', shell=False)
        if output and "HTTP Client import OK" in output:
            print("[+] Test 1: scienceskillscommon import - BERHASIL")
        else:
            print("[-] Test 1: scienceskillscommon import - GAGAL")
            tests_passed = False
    except Exception as e:
        print(f"[-] Test 1: scienceskillscommon import - GAGAL ({e})")
        tests_passed = False

    # Test 2: Verify docx node setup
    try:
        # Check node docx availability by running a quick node require check if node is on path
        if run_command("node -v"):
            node_code = "const docx = require('docx'); console.log('docx library OK');"
            output = run_command(f'node -e "{node_code}"', shell=False)
            if output and "docx library OK" in output:
                print("[+] Test 2: Node.js docx library - BERHASIL")
            else:
                print("[-] Test 2: Node.js docx library - GAGAL (Modul docx tidak ditemukan di global npm)")
                tests_passed = False
        else:
            print("[!] Test 2: Node.js docx library - DILEWATI (Node.js tidak terpasang di PATH)")
    except Exception as e:
        print(f"[-] Test 2: Node.js docx library - GAGAL ({e})")
        tests_passed = False

    if tests_passed:
        print("[+] Semua Smoke Test BERHASIL. Sistem terverifikasi stabil!")
    else:
        print("[!] Beberapa uji kelayakan gagal. Silakan periksa log setup di atas.")

def perform_update(dry_run=False):
    local_ver = get_local_version()
    remote_ver = get_remote_version()
    
    print(f"[*] Versi Lokal : {local_ver or 'Tidak terdeteksi'}")
    print(f"[*] Versi Online: {remote_ver or 'Tidak terdeteksi'}")
    
    if not remote_ver:
        print("[-] Gagal memproses update karena versi online tidak dapat dijangkau.")
        return
        
    if local_ver == remote_ver and not dry_run:
        print("[+] Versi lokal Anda sudah sama dengan versi online terbaru.")
        confirm = input("[?] Apakah Anda ingin memaksa pembaruan ulang? (y/N): ").strip().lower()
        if confirm != 'y':
            print("[*] Update dibatalkan.")
            return

    if dry_run:
        print("[*] Mode Dry-Run Aktif: Tidak ada perubahan yang akan ditulis ke disk.")
        return

    # Create safety backup
    create_backup()
    
    # Download and extract ZIP
    temp_zip = Path("template_update.zip")
    temp_dir = Path(".agents/temp_update")
    bridge_dir = Path(".agents/_bridge_update_")
    
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    if bridge_dir.exists():
        shutil.rmtree(bridge_dir)
        
    try:
        print("[*] Mengunduh paket pembaruan dari GitHub...")
        urllib.request.urlretrieve(ZIP_URL, temp_zip)
        
        print("[*] Mengekstrak paket pembaruan...")
        with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
            
        # Move extracted files to bridge folder
        extracted_folder = next(temp_dir.glob("Template-Research-*"))
        shutil.move(str(extracted_folder), str(bridge_dir))
        
        # Incremental Grafting & Copying
        print("[*] Menerapkan pembaruan berkas secara selektif...")
        
        # Engine and skill files to copy directly
        for src_path in bridge_dir.rglob("*"):
            if src_path.is_file():
                rel_path = src_path.relative_to(bridge_dir)
                
                # Exclude identity files from direct overwrite (prevent resetting user's info)
                if rel_path.name in ["gemini.md", "ACTION_PLAN.md", "word_sync_config.json"]:
                    # Merge logic or skip
                    if not Path(rel_path).exists():
                        # If not exists locally, copy it
                        Path(rel_path).parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(src_path, rel_path)
                    continue
                
                # Skip backups
                if "backups" in src_path.parts:
                    continue
                    
                # Copy engine, skills, and configuration files
                Path(rel_path).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_path, rel_path)
                
        print("[+] Semua berkas berhasil diperbarui.")
        
    finally:
        # Cleanup temporary zip files
        if temp_zip.exists():
            temp_zip.unlink()
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        if bridge_dir.exists():
            shutil.rmtree(bridge_dir)

    # Post update routines
    run_post_update_setups()
    run_smoke_test()
    print("[+] Pembaruan infrastruktur selesai dengan sukses!")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Template-Research Auto-Update Engine")
    parser.add_argument("--dry-run", action="store_true", help="Cek versi dan jalankan simulasi tanpa menulis berkas")
    parser.add_argument("--force", action="store_true", help="Paksa update tanpa konfirmasi")
    args = parser.parse_args()
    
    perform_update(dry_run=args.dry_run)
