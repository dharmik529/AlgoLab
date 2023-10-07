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