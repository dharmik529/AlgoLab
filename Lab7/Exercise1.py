class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

def kruskal(graph):
    # Sort the edges in non-decreasing order of their weights.
    graph.graph = sorted(graph.graph, key=lambda item: item[2])
    parent = [i for i in range(graph.V)]  # Initialize each vertex as its parent.
    mst = []  # Initialize an empty list to store the Minimum Spanning Tree edges.
    edges_added = 0  # Initialize the count of edges added to the MST.
    index = 0  # Initialize the index for iterating through sorted edges.

    while edges_added < graph.V - 1:
        u, v, w = graph.graph[index]
        index += 1
        x = find(parent, u)
        y = find(parent, v)

        # Check if adding the edge (u, v) would create a cycle in the MST.
        if x != y:
            mst.append((u, v, w))  # Add the edge to the MST.
            union(parent, x, y)  # Union the sets of vertices x and y.
            edges_added += 1

    return mst  # Return the Minimum Spanning Tree as a list of edges.

def find(parent, i):
    # Find the representative (root) of the set that contains vertex i.
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
    # Union two sets represented by x and y.
    x_set = find(parent, x)
    y_set = find(parent, y)
    parent[x_set] = y_set

# Example 1: Dense graph
g1 = Graph(4)
g1.add_edge(0, 1, 10)
g1.add_edge(0, 2, 6)
g1.add_edge(0, 3, 5)
g1.add_edge(1, 3, 15)
g1.add_edge(2, 3, 4)

mst1 = kruskal(g1)
print("Minimum Spanning Tree for Dense Graph:")
for u, v, w in mst1:
    print(f"{u} - {v}: {w}")

# Example 2: Sparse graph
g2 = Graph(5)
g2.add_edge(0, 1, 2)
g2.add_edge(0, 2, 1)
g2.add_edge(1, 2, 3)
g2.add_edge(1, 3, 4)
g2.add_edge(2, 4, 5)

mst2 = kruskal(g2)
print("Minimum Spanning Tree for Sparse Graph:")
for u, v, w in mst2:
    print(f"{u} - {v}: {w}")
