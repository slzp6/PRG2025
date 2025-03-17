""" p8_12.py """

import matplotlib.pyplot as plt
import networkx as nx

g1 = nx.gnp_random_graph(20, 0.30, 42)
mpos = nx.spring_layout(g1, seed=42)

plt.subplot(221)
nx.draw_networkx(g1, pos=mpos, \
               node_color='Cyan', \
               node_size=300, font_size=10)

g2 = nx.gnp_random_graph(20, 0.80, 43)
mpos = nx.spring_layout(g2, seed=42)
plt.subplot(222)
nx.draw_networkx(g2, pos=mpos, \
               node_color='Cyan', \
               node_size=300, font_size=10)

print('number of nodes:', g1.number_of_nodes())
print('number of edges:', g1.number_of_edges())
print('degree: ', g1.degree())
dh1 = nx.degree_histogram(g1)
print('degree histogram', dh1)

print('number of nodes:', g2.number_of_nodes())
print('number of edges:', g2.number_of_edges())
print('degree: ', g2.degree())
dh2 = nx.degree_histogram(g2)
print('degree histogram', dh2)

# len(dh2) > len(dh1)
dh1.extend([0] * (len(dh2) - len(dh1)))

plt.subplot(223)
plt.bar(range(len(dh1)), height=dh1)

plt.subplot(224)
plt.bar(range(len(dh2)), height=dh2)

# plt.show()
plt.savefig("p8_12.png")
