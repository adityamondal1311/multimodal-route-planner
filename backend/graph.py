import json
import networkx as nx

def load_graph(path="data/city_graph.json"):
    with open(path) as f:
        data = json.load(f)

    G = nx.Graph()

    for node, attr in data["nodes"].items():
        G.add_node(node, **attr)

    for edge in data["edges"]:
        G.add_edge(edge["from"], edge["to"],
                   weight=edge["weight"],
                   mode=edge["mode"])

    return G