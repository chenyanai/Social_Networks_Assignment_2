from collections import Counter

import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

graph = nx.read_gexf('net_il2015-2018.gexf')
print("Nodes before filtering: " + str(len(graph.nodes)))
print("Edges before filtering: " + str(len(graph.edges)))

# Selected only edges with weight 3 and above
edges = [edge for edge in graph.edges(data=True) if(edge[2]['weight'] >= 3)]

# Filter nodes and edges according to the rule above
# graph.edges = edges
selected_nodes = set()
for edge in edges:
    selected_nodes.add(edge[0])
    selected_nodes.add(edge[1])

all_node = set()
for n in graph.nodes():
    all_node.add(n)

graph.clear()
for i in edges:
    u = i[0]
    v = i[1]
    if u not in graph.nodes():
        graph.add_node(u)
    if v not in graph.nodes():
        graph.add_node(v)
    graph.add_edge(u, v, id=i[2]['id'], weight=i[2]['weight'])
for n in all_node:
    if n not in graph.nodes():
        graph.add_node(n)

print("Nodes after filtering: " + str(len(graph.nodes)))
print("Edges after filtering: " + str(len(graph.edges)))


degree_centrality_coefficient = nx.degree_centrality(graph)
values = Counter(degree_centrality_coefficient)
top_10_degree_cent = values.most_common(10)
graph_before_filter = nx.read_gexf('net_il2015-2018.gexf')
for node_id_dc in top_10_degree_cent:
    node_id = node_id_dc[0]
    node = graph_before_filter.nodes()[node_id]
    node_label = node['label']
    node_degree_centrality = node_id_dc[1]
    print(node_id, " :", node_label, " :", node_degree_centrality, " ")
print(nx.clustering(graph))
# print(nx.diameter(graph))