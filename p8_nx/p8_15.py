""" p8_15.py """

import matplotlib.pyplot as plt
import networkx as nx

g = nx.karate_club_graph()

pr = nx.pagerank(g)
node_color = list(pr.values())
print(pr)

pos = nx.spring_layout(g, seed=42)
nx.draw_networkx_edges(g, pos=pos)
nx.draw_networkx_nodes(g,
                       pos=pos,
                       node_size=700,
                       node_color=node_color,
                       cmap='viridis')
nx.draw_networkx_labels(g, pos=pos, font_size=15, font_color='white')
# plt.show()
plt.savefig("p8_15.png")
