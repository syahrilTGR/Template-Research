import json
import os
import subprocess
from pathlib import Path

# Config - Local Repo
REPO_ROOT = Path(os.getcwd())
GRAPH_OUT = REPO_ROOT / "graphify-out"
DETECT_JSON = GRAPH_OUT / ".graphify_detect.json"
GRAPH_JSON = GRAPH_OUT / "graph.json"

def run_cmd(cmd):
    print(f"Running: {cmd}")
    # Use powershell for better encoding handling in Windows
    full_cmd = f'powershell -ExecutionPolicy Bypass -Command "{cmd}"'
    result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout

def main():
    print(f"🚀 [LOCAL SKILL] Starting Comprehensive Brain Sync for: {REPO_ROOT.name}")
    
    if not GRAPH_OUT.exists():
        print(f"❌ Error: graphify-out not found in {REPO_ROOT}. Run graphify init first.")
        return

    # Step 1: Force Re-Detection
    print("--- Step 1: Re-detecting files (Code & Docs) ---")
    detect_py_code = """
import json
from graphify.detect import detect
from pathlib import Path
print("Scanning...")
result = detect(Path('.'))
with open('graphify-out/.graphify_detect.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2)
"""
    tmp_detect = REPO_ROOT / "tmp_detect_run.py"
    with open(tmp_detect, "w", encoding='utf-8') as f: f.write(detect_py_code)
    
    run_cmd(f"conda run -n train_mx150 python {tmp_detect.name}")
    if tmp_detect.exists(): os.remove(tmp_detect)

    # Step 2: AST Update
    print("--- Step 2: Updating AST (Code Structure) ---")
    run_cmd("conda run -n train_mx150 graphify update .")

    # Step 3: Pushing to Global Brain Center
    print("--- Step 3: Pushing to Global Brain Center ---")
    global_sync_script = REPO_ROOT / "scripts/update_global_brain.py"
    if global_sync_script.exists():
        run_cmd(f"conda run -n train_mx150 python {global_sync_script}")
    else:
        print("⚠️ Warning: scripts/update_global_brain.py not found. Skipping global sync.")
    
    print("\n✅ All systems synced successfully via Local Skill!")

if __name__ == "__main__":
    main()
