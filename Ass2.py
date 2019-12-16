from collections import Counter
import networkx as nx
from networkx.algorithms.community import girvan_newman
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw_graph = nx.read_gexf('net_il2015-2018.gexf')
print("Nodes before filtering: " + str(len(raw_graph.nodes)))
print("Edges before filtering: " + str(len(raw_graph.edges)))

# Selected only edges with weight 3 and above
edges = [edge for edge in raw_graph.edges(data=True) if(edge[2]['weight'] >= 3)]

# Filter nodes and edges according to the rule above
# graph.edges = edges
selected_nodes = set()
for edge in edges:
    selected_nodes.add(edge[0])
    selected_nodes.add(edge[1])

all_node = set()
for n in raw_graph.nodes():
    all_node.add(n)

nodes_with_data = raw_graph.nodes(data=True)

graph = nx.DiGraph()

for i in edges:
    u = i[0]
    v = i[1]
    if u not in graph.nodes():
        graph.add_node(str(u))
    if v not in graph.nodes():
        graph.add_node(str(v))
    graph.add_edge(u, v, id=i[2]['id'], weight=i[2]['weight'])
for n in all_node:
    if n not in graph.nodes():
        graph.add_node(str(n))

nx.set_node_attributes(graph, raw_graph.nodes(data=True)._nodes)

print("Nodes after filtering: " + str(len(graph.nodes)))
print("Edges after filtering: " + str(len(graph.edges)))


# first_iteration_comm = tuple(sorted(c) for c in next(gn_comm))
# dict(enumerate(first_iteration_comm))


# nx.draw_spring(graph, with_labels=True)


print(nx.clustering(graph))
# print(nx.diameter(graph))

# Adding parameters to each node:

clustering_coefficient_dict = nx.clustering(graph)
nx.set_node_attributes(G=graph, values=clustering_coefficient_dict, name='clustering coefficient')
# nx.set_edge_attributes(graph, clustering_coefficient_dict, 'clustering coefficient')

bc_results_dict = nx.betweenness_centrality(graph)
nx.set_node_attributes(graph, bc_results_dict, 'betweenness')

degree_centrality_coefficient = nx.degree_centrality(graph)
nx.set_node_attributes(graph, degree_centrality_coefficient, 'degree centrality')

eigenvector_centrality_dict = nx.eigenvector_centrality(graph, max_iter=900)
nx.set_node_attributes(graph, eigenvector_centrality_dict, 'eigenvector centrality')

closeness_centrality_dict = nx.closeness_centrality(graph)
nx.set_node_attributes(graph, closeness_centrality_dict, 'closeness centrality')

nodes_dict = dict()
nodes = graph.nodes(data=True)

for node in nodes:
    nodes_dict[node[0]] = node[1]

df = pd.DataFrame.from_dict(nodes_dict)
df = df.transpose()
df.to_csv('nodes.csv')
print(df)