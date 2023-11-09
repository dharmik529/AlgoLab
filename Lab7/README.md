# CMPSC 413 - Lab 7
## Minimum Spanning Tree

**Exercise1: 10 Points**

**Write the Kruskal’s algorithm and briefly explain the algorithm. Perform algorithm analysis to find the time complexity. Implement the Kruskal’s algorithm and test with minimum 2 graph examples. Use 1 example for a dense graph and 1 example for a sparse graph.**

Kruskal's algorithm is a widely used algorithm for finding the minimum spanning tree (MST) of a connected, undirected graph. The minimum spanning tree is a subset of the graph's edges that connects all the vertices while minimizing the total edge weight. The algorithm works as follows:

1. Initialize an empty set of edges, which will eventually form the minimum spanning tree. 
2. Sort all the edges in the graph in non-decreasing order of their weights. 
3. Start with the edge with the smallest weight.
4. Add the edge to the MST if adding it does not create a cycle in the MST.
5. Continue adding edges in increasing order of their weights while ensuring that no cycles are formed.
6. Repeat steps 4 and 5 until the MST contains V-1 edges, where V is the number of vertices in the graph.

Analysis - Time Complexity:

1. Sorting the edges takes O(E * log(E)) time, where E is the number of edges.
2. Initializing the empty set of edges takes O(E) time.
3. Checking for cycles can be efficiently done using a data structure like a disjoint-set (or union-find) data structure, which can perform operations like union and find in nearly constant time.
4. We perform E-1 iterations to add edges to the MST.
5. Overall, the time complexity of Kruskal's algorithm is O(E * log(E)) due to the sorting step.

**Exercise2: 10 Points**

**Write the Prim’s algorithm and briefly explain the algorithm. Perform algorithm analysis to find the time complexity. Implement the Prim’s algorithm and test with minimum 2 graph examples (use the same examples as in exercise-1).**

Prim's algorithm is a greedy algorithm used to find the minimum spanning tree (MST) of a connected, undirected graph. The MST is a subset of the graph's edges that connects all the vertices while minimizing the total edge weight. Prim's algorithm works as follows:

1. Initialize an empty set to represent the MST and a priority queue (min-heap) to store candidate edges.
2. Start with an arbitrary vertex as the initial MST, add it to the MST set, and enqueue its edges into the priority queue.
3. While the MST set does not contain all vertices:

    a. Remove the edge with the smallest weight from the priority queue.
    
    b. If one of the edge's vertices is already in the MST set and the other is not, add the non-MST vertex to the MST set and enqueue its edges.

4. Repeat step 3 until the MST contains all vertices.

Analysis - Time Complexity:

1. The priority queue operations (insertion, deletion, and retrieval of the minimum element) take O(log V) time, where V is the number of vertices.
2. In the worst case, all edges are processed, resulting in O(E) operations.
3. Therefore, the overall time complexity of Prim's algorithm is O(V log V + E).

**Exercise3: 10 Points**

**Discuss minimum 3 differences between Kruskal’s and Prim’s algorithm. Briefly explain any 2 practical applications.**

Deliverables: Report, codes and the demonstration video (~3 minutes)
For video demonstration, answer the following questions:
1. Using your codes, Explain the working of Kruskal’s algorithm?
2. Using your codes, Explain the working of Prim’s algorithm?
