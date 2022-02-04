import networkx as nx
from data import df_dist, df_time

def t_to_d(t):
    h, m = t.split(':')
    result = int(h) * 60 + int(m)
    return result

G = nx.DiGraph()

edges1 = []
edges2 = []
cities = list(df_dist.columns)
for i in cities:
    for j in cities:
        if i != j:
            edges1.append((i, j, {'dist': int(df_dist[i][j])}))
            edges2.append((i, j, {'time': t_to_d(df_time[i][j])}))

G.add_edges_from(edges1)
G.add_edges_from(edges2)

#print(G.get_edge_data('Bucaramanga', 'Pasto'))