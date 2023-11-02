def dfs(graph, start, visited=None):
    # If 'visited' is not provided, initialize it as an empty set
    if visited is None:
        visited = set()
    
    # Add the current node to the 'visited' set and print it
    visited.add(start)
    print(start, end=" ")

    # Explore neighbors of the current node
    for neighbor in graph[start]:
        if neighbor not in visited:
            # Recursively call DFS for unvisited neighbors
            dfs(graph, neighbor, visited)

# Define graph1
graph1 = {
    "a": ["d", "f"],
    "b": ["c"],
    "c": ["b", "c", "d", "e"],
    "d": ["a", "c"],
    "e": ["c"],
    "f": ["a"]
}

# Perform DFS on graph1 starting from node 'a'
print("DFS on graph1:")
dfs(graph1, 'a')

# Define graph2
graph2 = {
    "a": ["d", "f"],
    "b": ["c", "b"],
    "c": ["b", "c", "d", "e"],
    "d": ["a", "c"],
    "e": ["c"],
    "f": ["a"]
}

# Perform DFS on graph2 starting from node 'a'
print("\nDFS on graph2:")
dfs(graph2, 'a')
