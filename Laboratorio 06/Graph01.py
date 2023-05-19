import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo vacío
G = nx.Graph()

# Agregar nodos al grafo
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Agregar conexiones entre nodos
G.add_edge(1, 2)
G.add_edge(2, 3)

# Dibujar el grafo
nx.draw(G, with_labels=True)

# Mostrar el grafo
plt.show()