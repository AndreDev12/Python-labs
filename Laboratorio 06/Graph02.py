import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo vacío
G = nx.Graph()

# Agregar nodosal grafo
G.add_node('Padre')
G.add_node('Hijo 1')
G.add_node('Hijo 2')

# Agregar conexiones entre nodos
G.add_edge('Padre', 'Hijo 1')
G.add_edge('Padre', 'Hijo 2')

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)

# Mostrar el grafo
plt.show()