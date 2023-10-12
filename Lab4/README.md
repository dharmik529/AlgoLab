# CMPSC 413 - Lab 4
## Priority queue, and Heap Sort

### Lab Exercises
The priority queue is an abstract data type that contains the following methods:
- insert(item, priorityValue)
&nbsp;&nbsp;&nbsp;&nbsp; Inserts item into the priority queue with priority value priorityValue.
- peek()
&nbsp;&nbsp;&nbsp;&nbsp; Returns (but does not remove) the item with highest priority in the priority queue.
- delete()
&nbsp;&nbsp;&nbsp;&nbsp; Removes and returns the item with highest priority in the priority queue.
- changePriority(item, newPriority)
&nbsp;&nbsp;&nbsp;&nbsp; Changes the priority of an item to a new priority value.

### Exercise 1
Write down the algorithm and implement a priority queue (both min and max) using an array of elements. Determine the runtime for each of the following:

1. In the worst case, describe the runtime to insert an item into the priority queue.
2. In the worst case, describe the runtime to remove the element with highest priority.
3. In the worst case, describe the runtime to change the priority of an element (find an element and change the priority of the element).

Show an example for each.

**Runtime complexities are:**
1. Insert: When inserting an item, the worst-case runtime occurs when the item needs to be moved to the root of the heap (due to higher priority) or all the way down to the last level. This results in a time complexity of O(log N), where N is the number of elements in the priority queue.
2. Delete: In the worst case, when you delete an item, you need to perform the heapify operation to maintain the heap property. This operation also has a time complexity of O(log N) as it involves moving elements within the heap.
3. Change: In the worst case, you might need to move an element up to the root or all the way down to the last level, which is also O(log N).

These time complexities assume a balanced heap, and in practice, heaps provide efficient operations for priority queues. However, it's important to note that these are worst-case complexities, and the average-case performance might be better, depending on the distribution of priorities and items.

### Exercise 2 
Write down the algorithm and implement a priority queue (both min and max) using a linked list of elements. Determine the runtime for each of the following:

1. In the worst case, describe the runtime to insert an item into the priority queue.
2. In the worst case, describe the runtime to remove the element with highest priority.
3. In the worst case, describe the runtime to change the priority of an element.

Show an example for each.

**Runtime complexities are:**
1. Insert: In the worst case, for insertion, you may need to traverse the entire linked list to find the correct position for the new element. This results in a time complexity of O(N), where N is the number of elements in the priority queue.
2. Delete: Deletion involves updating the head of the linked list. This operation has a time complexity of O(1) in the worst case.
3. Change: Changing the priority involves searching for the element in the linked list and rearranging it if its priority has increased. In the worst case, this operation is O(N) because you may need to traverse the entire list to find the item.

These time complexities reflect the worst-case scenario and assume no additional data structures or optimizations. Linked list implementations are less efficient than heap-based implementations for large priority queues, but they are straightforward to implement and suitable for small-sized priority queues or when dynamic resizing is not a concern.

### Exercise 3 
Write down the algorithm and implement a priority queue (both min and max) using a heap tree-based data structure (both min and max). Determine the runtime for each of the following:

1. In the worst case, describe the runtime to insert an item into the priority queue.
2. In the worst case, describe the runtime to remove the element with highest priority.
3. In the worst case, describe the runtime to change the priority of an element.

Show an example for each.

**Runtime complexities are:**
1. Insert: In a binary heap-based implementation, insertion takes O(log N) time in the worst case, where N is the number of elements in the heap. This is because you may need to perform "up-heap" operations to maintain the heap property.
2. Delete: Deletion, which includes finding and removing the element with the highest priority, also takes O(log N) time in the worst case. This is because you need to perform "down-heap" operations to maintain the heap property after removing the root element.
3. Change: Changing the priority of an element involves finding the item in the heap and then possibly performing heap operations. Finding the element is O(N) in the worst case, and then the subsequent heapify operation is O(log N).

Heap-based priority queues are efficient for many practical use cases because they maintain the highest or lowest priority element at the root, allowing quick access to it. The worst-case time complexities described here are based on a balanced heap.

### Exercise 4 
Tabulate to compare the time complexity of insert, remove and change priority operations for array/linked list/ heap priority queues.

| **Operation** | **Array**    | **Linked-List** | **Min-Heap** | **Max-Heap** |
|---------------|--------------|-----------------|--------------|--------------|
| Insertion     | O(1) or O(N) | O(N)            | O(log N)     | O(log N)     |
| Deletion      | O(N) or O(1) | O(1)            | O(log N)     | O(log N)     |
| Changing      | O(N)         | O(N)            | O(N + log N) | O(N + log N) |



### Exercise 5 
Write a paragraph about what have you learnt from this lab exercises?

In summary, the choice of data structure depends on the specific use case and the relative importance of different operations. Arrays and linked lists are straightforward to implement but may not be the most efficient choice for large priority queues. Heap-based structures provide better performance for insert and remove operations, but changing the priority remains relatively expensive. The choice between min-heap and max-heap depends on whether you need the highest or lowest priority element to be easily accessible.

### Deliverables

- Codes
- Report with algorithms, screenshots of results for each exercise and conclusion
- Attach the codes as appendix in your Report
- Recorded zoom video (~5 minutes) explaining the difference in implementation of priority queues using different data structures and also demonstrate the working of the program.

