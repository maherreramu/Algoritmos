import networkx as nx
from graph import G, cities

#st = nodo inicio
#end = nodo final
#mode = 'dist' o 'time'
def nx_dijkstra(st, end, mode):
    if mode == 'dist' or mode == 'time':
        if cities.index(st) and cities.index(end):
            path = nx.shortest_path(G, source=st, target=end, weight=mode)

            data = 0
            if len(path) < 3:
                data = G.get_edge_data(cities[0], cities[1])[mode]
            else:
                for i in range(0, len(path)-1):
                    G.get_edge_data(cities[i], cities[i+1])[mode]
                    
            if mode == 'time':
                m = data%60
                h = (data-m)/60
                data = h+":"+m

            return (path, data)

nx_dijkstra('Cali', 'Bucaramanga', 'dist')