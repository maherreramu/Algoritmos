import networkx as nx
import matplotlib.pyplot as plt
from graph import G

plot = nx.spring_layout(G)

nx.draw_networkx_nodes(G, plot)
nx.draw_networkx_edges(G, plot, edgelist=G.edges())
nx.draw_networkx_labels(G, plot)
plt.show()