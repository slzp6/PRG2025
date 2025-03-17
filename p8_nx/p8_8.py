""" p8_8.py """

import networkx as nx
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4, 16))

plt.subplot(411)
g_grid = nx.grid_2d_graph(7, 5)
mpos = nx.spring_layout(g_grid)
nx.draw(g_grid, pos=mpos, with_labels=True, node_color="skyblue")

plt.subplot(412)
g_ladder = nx.ladder_graph(10)
mpos = nx.spring_layout(g_ladder)
nx.draw(g_ladder, pos=mpos, with_labels=True, node_color="skyblue")

plt.subplot(413)
g_lollipop = nx.lollipop_graph(6, 4)
mpos = nx.spring_layout(g_lollipop, seed=42)
nx.draw(g_lollipop, pos=mpos, with_labels=True, node_color="skyblue")

plt.subplot(414)
g_wheel = nx.wheel_graph(10)
mpos = nx.spring_layout(g_wheel, seed=42)
nx.draw(g_wheel, pos=mpos, with_labels=True, node_color="skyblue")

# plt.show()
plt.savefig("p8_8.png")
