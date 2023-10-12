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
1. Insert: O(n) - Need to sort the entire array after each insert in worst case
2. Remove highest priority: O(1) - Just pop from the front of the array
3. Change priority: O(n) - Need to find the element first (linear search) and then resort the array

The priority queue operations have O(n) runtime in the worst case using an array implementation because of the need to search and sort the array. More efficient implementations use heaps or specialized tree data structures.

### Exercise 2 
Write down the algorithm and implement a priority queue (both min and max) using a linked list of elements. Determine the runtime for each of the following:

1. In the worst case, describe the runtime to insert an item into the priority queue.
2. In the worst case, describe the runtime to remove the element with highest priority.
3. In the worst case, describe the runtime to change the priority of an element.

Show an example for each.

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

