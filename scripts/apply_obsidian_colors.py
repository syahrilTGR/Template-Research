import json
import os
import colorsys
from pathlib import Path

# --- CONFIG ---
# Use Path.home() for portability
GRAPH_CONFIG = Path.home() / "Documents" / "Brain-Global-Center" / ".obsidian" / "graph.json"
NUM_COMMUNITIES = 50 # Over-estimate to cover all possible hubs

def get_neon_colors(n):
    colors = []
    for i in range(n):
        hue = i / n
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        r, g, b = [int(x * 255) for x in rgb]
        hex_int = (r << 16) | (g << 8) | b
        colors.append(hex_int)
    return colors

def apply_neon_colors():
    print(f"🎨 Applying Neon Aesthetics to: {GRAPH_CONFIG}")
    if not GRAPH_CONFIG.exists():
        print(f"⚠️ Warning: Obsidian graph config not found at {GRAPH_CONFIG}. Skipping.")
        return

    with open(GRAPH_CONFIG, 'r', encoding='utf-8') as f:
        config = json.load(f)

    palette = get_neon_colors(NUM_COMMUNITIES)
    color_groups = []

    for cid in range(NUM_COMMUNITIES):
        color_groups.append({
            "query": f"tag:#community/Community_{cid}",
            "color": {
                "a": 1,
                "rgb": palette[cid]
            }
        })

    config["colorGroups"] = color_groups
    
    # NEON THEME BOOSTS
    config["showArrow"] = True
    config["showLabels"] = True
    config["labelSizeMultiplier"] = 1.1
    config["nodeSizeMultiplier"] = 1.4
    config["lineSizeMultiplier"] = 0.6 
    config["centerStrength"] = 0.5
    config["repelStrength"] = 15 
    config["linkDistance"] = 200

    with open(GRAPH_CONFIG, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)

    print(f"✅ Success. Applied {NUM_COMMUNITIES} NEON color groups.")

if __name__ == "__main__":
    apply_neon_colors()
