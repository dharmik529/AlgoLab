class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        # Add an edge to the graph with vertices u, v, and weight w.
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

def prim(graph):
    MST = []
    visited = [False] * graph.V
    key = [float('inf')] * graph.V  # Initialize key values as infinity for all vertices.
    parent = [-1] * graph.V  # Initialize parent values as -1 for all vertices.

    # Start with the first vertex as the root.
    key[0] = 0

    for _ in range(graph.V):
        # Find the vertex with the minimum key value among the vertices not yet included in MST.
        min_key = float('inf')
        for v in range(graph.V):
            if not visited[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        visited[u] = True

        # Update key and parent values of adjacent vertices.
        for neighbor, edge_weight in graph.graph[u]:
            if not visited[neighbor] and edge_weight < key[neighbor]:
                key[neighbor] = edge_weight
                parent[neighbor] = u

    # Construct the MST using the parent array.
    for v in range(1, graph.V):
        MST.append((parent[v], v))

    return MST

# Example 1: Dense graph
g1 = Graph(4)
g1.add_edge(0, 1, 10)
g1.add_edge(0, 2, 6)
g1.add_edge(0, 3, 5)
g1.add_edge(1, 3, 15)
g1.add_edge(2, 3, 4)

mst1 = prim(g1)
print("Minimum Spanning Tree for Dense Graph:")
for u, v in mst1:
    print(f"{u} - {v}")

# Example 2: Sparse graph
g2 = Graph(5)
g2.add_edge(0, 1, 2)
g2.add_edge(0, 2, 1)
g2.add_edge(1, 2, 3)
g2.add_edge(1, 3, 4)
g2.add_edge(2, 4, 5)

mst2 = prim(g2)
print("Minimum Spanning Tree for Sparse Graph:")
for u, v in mst2:
    print(f"{u} - {v}")
