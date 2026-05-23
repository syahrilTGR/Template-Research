"""Sync Check Utility for Office files.

Audits whether the unpacked XML files are out of sync with the main Office document (DOCX, PPTX, XLSX), indicating the user has made manual edits since the last pack/unpack operation.

Usage:
    python sync_check.py <unpacked_dir> <docx_file> [--auto-unpack true|false]
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


def sync_check(unpacked_dir: str, docx_file: str, auto_unpack: bool = True) -> int:
    unpacked_path = Path(unpacked_dir)
    docx_path = Path(docx_file)
    last_sync_path = unpacked_path / ".last_sync.json"

    print("--- Antigravity Sync Audit Tool ---")
    print(f"Auditing unpacked directory: {unpacked_path.name}")
    print(f"Against source document:     {docx_path.name}")

    if not docx_path.exists():
        print(f"[ERROR] Source document does not exist: {docx_path}")
        return 1

    # Get current stats of the docx file
    try:
        docx_stat = docx_path.stat()
        curr_mtime = docx_stat.st_mtime
        curr_size = docx_stat.st_size
    except Exception as e:
        print(f"[ERROR] Failed to read source file stats: {e}")
        return 1

    # Check if metadata exists
    if not last_sync_path.exists():
        print("[WARNING] No sync metadata file (.last_sync.json) found in the unpacked directory.")
        if auto_unpack:
            print("Running initial unpack to synchronize directory and establish metadata...")
            return _run_unpack(docx_path, unpacked_path)
        else:
            print("[STATUS] NO_METADATA (Requires unpacking to initialize tracking)")
            return 1

    # Load saved metadata
    try:
        metadata = json.loads(last_sync_path.read_text(encoding="utf-8"))
        saved_mtime = metadata.get("mtime", 0.0)
        saved_size = metadata.get("size", 0)
    except Exception as e:
        print(f"[ERROR] Failed to read sync metadata file: {e}")
        if auto_unpack:
            print("Re-unpacking directory to resolve corruption...")
            return _run_unpack(docx_path, unpacked_path)
        else:
            print("[STATUS] CORRUPT_METADATA")
            return 1

    # Compare. Allow 2.0 seconds tolerance for filesystem timestamp precision differences
    time_diff = curr_mtime - saved_mtime
    size_diff = curr_size != saved_size

    if time_diff > 2.0 or size_diff:
        print("\n[OUT_OF_SYNC] The source Word document has newer manual changes!")
        print(f"  Saved  -> mtime: {saved_mtime:.1f}, size: {saved_size} bytes")
        print(f"  Actual -> mtime: {curr_mtime:.1f}, size: {curr_size} bytes")
        
        if auto_unpack:
            print("\nAuto-unpack is ACTIVE. Synchronizing manual changes back into XML folder...")
            return _run_unpack(docx_path, unpacked_path)
        else:
            print("\n[STATUS] OUT_OF_SYNC (Please run unpack.py to pull manual changes first!)")
            return 1
    else:
        print("\n[IN_SYNC] The unpacked XML folder is completely up to date with the Word document.")
        print(f"  Last synchronized state: mtime={saved_mtime:.1f}, size={saved_size} bytes")
        return 0


def _run_unpack(docx_path: Path, unpacked_path: Path) -> int:
    script_dir = Path(__file__).parent
    unpack_script = script_dir / "unpack.py"

    cmd = [
        sys.executable,
        str(unpack_script),
        str(docx_path),
        str(unpacked_path)
    ]
    
    print(f"Running: {' '.join(cmd)}")
    
    # Force UTF-8 encoding for output print safely
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"

    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if res.returncode == 0:
        print(res.stdout)
        print("[SUCCESS] Synchronization complete! Unpacked XML files are now updated.")
        return 0
    else:
        print(f"[ERROR] Auto-unpack failed (exit code: {res.returncode}):")
        print(res.stderr)
        return res.returncode


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Verify if unpacked directory is in sync with the source document"
    )
    parser.add_argument("unpacked_directory", help="Unpacked document directory")
    parser.add_argument("docx_file", help="Main Office document file (.docx/.pptx/.xlsx)")
    parser.add_argument(
        "--auto-unpack",
        type=lambda x: x.lower() == "true",
        default=True,
        metavar="true|false",
        help="Automatically unpack and sync if out of sync (default: true)",
    )
    args = parser.parse_args()

    exit_code = sync_check(
        args.unpacked_directory,
        args.docx_file,
        auto_unpack=args.auto_unpack
    )
    sys.exit(exit_code)
