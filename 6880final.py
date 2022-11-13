import networkx as nx

import matplotlib.pyplot as plt

from matplotlib import animation, rc

from random import randint, uniform

import plotly.graph_objects as go

rc('animation', html='html5')

'''

NUM_NODES = 40

def random_node():

    return randint(0, NUM_NODES-1)

def random_weight():

    return uniform(0, 1)

G = nx.Graph()

for i in range(1, NUM_NODES):

    G.add_edge(i-1, i, weight=random_weight())

for _ in range(NUM_NODES * 2):

    G.add_edge(

        random_node(), random_node(), weight=random_weight()

    )

'''

#G = nx.Graph()

G = nx.random_geometric_graph(20, .5)

edge_x = []

edge_y = []

for edge in G.edges():

    x0, y0 = G.nodes[edge[0]]['pos']

    x1, y1 = G.nodes[edge[1]]['pos']

    edge_x.append(x0)

    edge_x.append(x1)

    edge_x.append(None)

    edge_y.append(y0)

    edge_y.append(y1)

    edge_y.append(None)

edge_trace = go.Scatter(

    x=edge_x, y=edge_y,

    line=dict(width=0.5, color='#888'),

    hoverinfo='none',

    mode='lines')

node_x = []

node_y = []

for node in G.nodes():

    x, y = G.nodes[node]['pos']

    node_x.append(x)

    node_y.append(y)

print(G)

pos = nx.spring_layout(G)

nx.draw(G,pos,node_color='k')

# draw path in red

path = nx.shortest_path(G,source=1,target=19)

path_edges = list(zip(path,path[1:]))

nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')

nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=5)

plt.axis('equal')

plt.show()
