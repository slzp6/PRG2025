""" p8_24.py """

# https://snap.stanford.edu/data/ego-Facebook.html
# !curl https://snap.stanford.edu/data/facebook_combined.txt.gz --output facebook_combined.txt.gz
#
# Get! "facebook_combined.txt.gz"

# pylint: disable=pointless-string-statement
'''
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

facebook = pd.read_csv(
    "facebook_combined.txt.gz",
    compression="gzip",
    sep=" ",
    names=["start_node", "end_node"],
)
print(facebook)

g = nx.from_pandas_edgelist(facebook, "start_node", "end_node")

pos = nx.spring_layout(g, iterations=30, seed=42)
fig, ax = plt.subplots(figsize=(15, 9))
ax.axis("off")
nx.draw_networkx(g, pos=pos, ax=ax, node_size=5, with_labels=False)
# plt.show()
plt.savefig("p8_24.png")

print(g.number_of_nodes())
print(g.number_of_edges())
print(nx.number_connected_components(g))
print(np.mean(list(dict(g.degree()).values())))

'''
