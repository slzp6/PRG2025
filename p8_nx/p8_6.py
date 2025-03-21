""" p8_6.py """

import matplotlib.pyplot as plt
import networkx as nx

g = nx.cycle_graph(10)

mpos = nx.spring_layout(g)
nx.draw_networkx(g, pos=mpos, \
                 node_color='Cyan', \
                     node_size=500, \
                         font_size=20)
# plt.show()
plt.savefig("p8_6.png")
