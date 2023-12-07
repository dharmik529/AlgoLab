import networkx as nx
import heapq

class RoutingGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, node1, node2, weight):
        self.graph.add_edge(node1, node2, weight=weight)
        self.graph.add_edge(node2, node1, weight=weight)

    def dijkstra_shortest_path(self, source, destination):
        distances = {node: float('inf') for node in self.graph.nodes}
        distances[source] = 0
        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight['weight']
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances[destination]

    def bellman_ford_shortest_path(self, source, destination):
        distances = {node: float('inf') for node in self.graph.nodes}
        distances[source] = 0

        for _ in range(len(self.graph.nodes) - 1):
            for node1, node2, weight in self.graph.edges(data='weight'):
                if distances[node1] + weight < distances[node2]:
                    distances[node2] = distances[node1] + weight

        return distances[destination]

# Example Usage
routing_graph = RoutingGraph()
routing_graph.add_edge('A', 'B', 1)
routing_graph.add_edge('A', 'C', 3)
routing_graph.add_edge('B', 'D', 2)
routing_graph.add_edge('C', 'D', 1)
routing_graph.add_edge('D', 'E', 3)

# Dijkstra's algorithm
dijkstra_result = routing_graph.dijkstra_shortest_path('A', 'E')
print(f'Dijkstra\'s Shortest Path: {dijkstra_result}')

# Bellman-Ford algorithm
bellman_ford_result = routing_graph.bellman_ford_shortest_path('A', 'E')
print(f'Bellman-Ford Shortest Path: {bellman_ford_result}')

