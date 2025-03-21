""" p8_11.py """

import matplotlib.pyplot as plt
import networkx as nx

fig = plt.figure(figsize=(8, 12))
plt.subplot(211)
g = nx.gnp_random_graph(30, 0.20, 1579452)
mpos = nx.spring_layout(g, seed=80386)
nx.draw_networkx(g, pos=mpos, \
               node_color='Cyan', \
               node_size=300, font_size=10)

print('number of nodes:', g.number_of_nodes())
print('number of edges:', g.number_of_edges())
print('degree: ', g.degree())
dh = nx.degree_histogram(g)
print('degree histogram', dh)
plt.subplot(212)
plt.bar(range(len(dh)), height=dh)
# plt.show()
plt.savefig("p8_11.png")
