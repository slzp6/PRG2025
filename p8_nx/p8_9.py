""" p8_9.py """

import matplotlib.pyplot as plt
import networkx as nx

g = nx.DiGraph()

nodes = ['a', 'b', 'c', 'd', 'e']
edges = [('a', 'b'), ('a', 'c'), ('a', 'e'),\
         ('b', 'd'), ('b', 'e'),\
         ('c', 'e'), ('d', 'e')]

g.add_nodes_from(nodes)
g.add_edges_from(edges)

mpos = nx.spring_layout(g, seed=42)
nx.draw_networkx(g, pos=mpos, \
                node_color='Cyan', \
                node_size=1000, font_size=25)
# plt.show()
plt.savefig("p8_9.png")
