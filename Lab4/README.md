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

### Exercise 4 
Tabulate to compare the time complexity of insert, remove and change priority operations for array/linked list/ heap priority queues.

### Exercise 5 
Write a paragraph about what have you learnt from this lab exercises?

### Deliverables

- Codes
- Report with algorithms, screenshots of results for each exercise and conclusion
- Attach the codes as appendix in your Report
- Recorded zoom video (~5 minutes) explaining the difference in implementation of priority queues using different data structures and also demonstrate the working of the program.

