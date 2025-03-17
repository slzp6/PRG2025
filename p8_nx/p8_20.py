""" p8_20.py """

import matplotlib.pyplot as plt
import networkx as nx

graph_a = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': [],
    'd': ['f'],
    'e': ['g', 'h'],
    'f': [],
    'g': ['h'],
    'h': []
}

g = nx.from_dict_of_lists(graph_a)
mpos = nx.spring_layout(g, seed=2618586)
nx.draw_networkx(g, pos=mpos, \
                 node_color='Cyan', \
                 node_size=800, \
                 font_size=25)
# plt.show()
plt.savefig("p8_20.png")
