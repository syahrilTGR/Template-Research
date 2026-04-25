import json
import os
from pathlib import Path
from collections import defaultdict
from graphify.build import build_from_json
from graphify.export import to_obsidian, to_canvas

# --- CONFIG ---
# Use Path.home() and Path.cwd() for full portability
BASE_PATH = Path.home() / "Documents" / "Brain-Global-Center"
GRAPH_JSON = Path.cwd() / "graphify-out" / "graph.json"
NODES_SUBDIR = BASE_PATH / "nodes"

def export_official():
    print(f"📦 Exporting Official Vault Structure to: {BASE_PATH}")
    if not GRAPH_JSON.exists():
        print(f"❌ Error: Local graph.json not found at {GRAPH_JSON}")
        return

    # 1. Load Graph
    with open(GRAPH_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    G = build_from_json(data)
    
    # 2. Group Nodes by Community
    communities = defaultdict(list)
    for n in G.nodes:
        cid = G.nodes[n].get('community', 0)
        communities[cid].append(n)
    
    # 3. Export Nodes to subfolder
    os.makedirs(NODES_SUBDIR, exist_ok=True)
    to_obsidian(G, communities, str(NODES_SUBDIR))
    
    # 4. Export Canvas to root
    to_canvas(G, communities, str(BASE_PATH / "graph.canvas"))
    
    # 5. Move Community Hubs to Root for easy access
    print("🚀 Finalizing Vault Hierarchy...")
    for filename in os.listdir(NODES_SUBDIR):
        if filename.startswith("_COMMUNITY_"):
            source = NODES_SUBDIR / filename
            target = BASE_PATH / filename
            if target.exists(): os.remove(target)
            os.rename(source, target)

    print(f"✅ Success! Official vault generated at {BASE_PATH}")

if __name__ == "__main__":
    export_official()
