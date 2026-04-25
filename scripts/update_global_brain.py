import json
from pathlib import Path
import networkx as nx
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json, to_obsidian

# 1. Load the master graph
# NOTE: center_path represents your Global Knowledge Center location.
center_path = Path.home() / "Documents" / "Brain-Global-Center"
# 1. Load the local graph (Source of Truth for updates)
# Use dynamic path resolution for portability
local_graph_path = Path.cwd() / "graphify-out" / "graph.json"
graph_path = center_path / "global-graph.json"

if local_graph_path.exists():
    print(f"Syncing from local graph: {local_graph_path}")
    with open(local_graph_path, 'r', encoding='utf-8') as f:
        master_data = json.load(f)
else:
    print(f"Local graph not found, falling back to global: {graph_path}")
    with open(graph_path, 'r', encoding='utf-8') as f:
        master_data = json.load(f)

# 2. Build NetworkX graph from the JSON
# Handle both simple graphify schema and networkx schema
G = nx.Graph()
for node in master_data.get('nodes', []):
    G.add_node(node['id'], **node)

# Handle both 'edges' and 'links' keys
edge_data = master_data.get('edges', master_data.get('links', []))
for edge in edge_data:
    G.add_edge(edge['source'], edge['target'], **edge)

print(f"Graph loaded: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges.")

# 3. Re-cluster
communities = cluster(G)
cohesion = score_all(G, communities)
gods = god_nodes(G)
surprises = surprising_connections(G, communities)
labels = {cid: f"Community {cid}" for cid in communities}
questions = suggest_questions(G, communities, labels)

# 4. Save Updated JSON & Obsidian
to_json(G, communities, str(graph_path))
to_obsidian(G, communities, str(center_path / "Obsidian-Vault"), community_labels=labels)

# 5. Generate Updated Report
detection_summary = {"total_files": G.number_of_nodes(), "total_words": 0}
report = generate(G, communities, cohesion, labels, gods, surprises, detection_summary, {"input":0, "output":0}, str(Path.cwd()), suggested_questions=questions)
(center_path / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")

print(f"Global Research Brain Finalized!")
print(f"Updated Report saved to {center_path / 'GRAPH_REPORT.md'}")
