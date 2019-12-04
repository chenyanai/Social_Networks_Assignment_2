import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

graph = nx.read_gexf('net_il2015-2018.gexf')
print(len(graph.nodes))
print(len(graph.edges))

# Selected only edges with weight 3 and above
edges = [edge for edge in graph.edges(data=True) if(edge[2]['weight'] >= 3)]

# Filter nodes and edges according to the rule above
# graph.edges = edges
selected_nodes = set()
for edge in edges:
    selected_nodes.add(edge[0])
    selected_nodes.add(edge[1])
graph = graph.subgraph(selected_nodes)
print(len(graph.nodes))
print(len(graph.edges))

print(nx.clustering(graph))
# print(nx.diameter(graph))