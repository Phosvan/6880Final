from __future__ import print_function, division
import networkx as nx
import matplotlib.pyplot as plt

N=20
G=nx.grid_2d_graph(N,N)
pos = dict( (n, n) for n in G.nodes() )
labels = dict( ((i, j), i + (N-1-j) * N ) for i, j in G.nodes() )
nx.relabel_nodes(G,labels,False)
inds=list(labels)
vals=list(labels.values())
inds.sort()
vals.sort()
pos2=dict(zip(vals,inds))
nx.draw_networkx(G, pos=pos2, with_labels=False, node_size = 15)

T=nx.minimum_spanning_tree(G)

plt.figure()
nx.draw_networkx(T, pos=pos2, with_labels=False, node_size = 15)
plt.show()