from collections import deque

def bfs(graph, start):
    # Create an empty set to keep track of visited nodes
    visited = set()
    # Create a queue for BFS using a deque
    queue = deque([start])
    # Mark the start node as visited
    visited.add(start)

    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        # Print the current node (you can modify this to store or process the node as needed)
        print(node, end=" ")

        # Explore neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Mark the neighbor as visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

# Define graph1
graph1 = {
    "a": ["d", "f"],
    "b": ["c"],
    "c": ["b", "c", "d", "e"],
    "d": ["a", "c"],
    "e": ["c"],
    "f": ["a"]
}

# Perform BFS on graph1 starting from node 'a'
print("BFS on graph1:")
bfs(graph1, 'a')

# Define graph2
graph2 = {
    "a": ["d", "f"],
    "b": ["c", "b"],
    "c": ["b", "c", "d", "e"],
    "d": ["a", "c"],
    "e": ["c"],
    "f": ["a"]
}

# Perform BFS on graph2 starting from node 'a'
print("\nBFS on graph2:")
bfs(graph2, 'a')

