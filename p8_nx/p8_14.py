""" p8_14.py """

import matplotlib.pyplot as plt
import networkx as nx

g = nx.karate_club_graph()
pos = nx.spring_layout(g, seed=42)
nx.draw_networkx(g, pos=pos)
# plt.show()
plt.savefig("p8_14.png")
