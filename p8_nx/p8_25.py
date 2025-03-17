""" p8_25.py """

# Make sure to install pyvis
# https://pyvis.readthedocs.io/
#
# conda install conda-forge::pyvis

# pylint: disable=pointless-string-statement
'''
from pyvis import network as net
import networkx as nx

g = net.Network()
g_karate = nx.karate_club_graph()
g.from_nx(g_karate)

for node in g.get_nodes():
    g.get_node(node)['label'] = str(node)

g.save_graph("p8_25.html")

'''
