""" p8_5.py """

import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()
nodes = ['a', 'b', 'c', 'd', 'e']
edges = [('a', 'b'), ('a', 'c'), \
         ('a', 'd'), ('b', 'd'), \
         ('c', 'd'), ('d', 'e')]

g.add_nodes_from(nodes)
g.add_edges_from(edges)

S = 'a'
T = 'e'
path_all = list(nx.all_simple_paths(g, S, T))
path_shortest = nx.shortest_path(g, S, T)

print(f"all path(s): {path_all}")
print(f"shortest path: {path_shortest}")

mpos = nx.spring_layout(g, seed=42)
nx.draw_networkx(g, pos=mpos, \
                node_color='Cyan', \
                node_size=1000, font_size=25)
# plt.show()
plt.savefig("p8_5.png")
