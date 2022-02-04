import networkx as nx
from graph import G

path = nx.shortest_path(G, source='Cali', target='Bucaramanga', weight='dist')
print(path)