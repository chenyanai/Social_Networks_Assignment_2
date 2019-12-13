from collections import Counter
import networkx as nx
from networkx.algorithms.community import girvan_newman
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


# first_iteration_comm = tuple(sorted(c) for c in next(gn_comm))
# dict(enumerate(first_iteration_comm))


# nx.draw_spring(graph, with_labels=True)


print(nx.clustering(graph))
# print(nx.diameter(graph))