import networkx as nx

#criando o grafo:
grafo = nx.Graph()
#adicionando vertices
grafo.add_node(2)
grafo.add_nodes_from([3, 6, 1, 7])

#adicionando arestas
grafo.add_edge(3, 6)
grafo.add_edges_from([(3, 1), (7, 6)])

print "numero de vertices: ", grafo.number_of_nodes()
print "numero de arestas: ", grafo.number_of_edges()
print "vizinhos do vertice 3: ", grafo.neighbors(3)
print "grau do vertice 3: ", grafo.degree(3)

