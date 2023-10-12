import heapq

class PriorityQueue:
    def __init__(self, is_max_heap=False):
        self.heap = []
        self.is_max_heap = is_max_heap

    def insert(self, item, priorityValue):
        if self.is_max_heap:
            priorityValue = -priorityValue
        heapq.heappush(self.heap, (priorityValue, item))

    def peek(self):
        if not self.heap:
            return None
        if self.is_max_heap:
            return self.heap[0][1]
        return self.heap[0][1]

    def delete(self):
        if not self.heap:
            return None
        _, item = heapq.heappop(self.heap)
        return item

    def changePriority(self, item, newPriority):
        if self.is_max_heap:
            newPriority = -newPriority

        # Find the item in the heap
        for i, (priority, existing_item) in enumerate(self.heap):
            if existing_item == item:
                self.heap[i] = (newPriority, item)
                heapq.heapify(self.heap)  # Rebuild the heap

# Example usage
min_priority_queue = PriorityQueue()
max_priority_queue = PriorityQueue(is_max_heap=True)

# Insertion in both queues
min_priority_queue.insert('A', 5)
min_priority_queue.insert('B', 3)
min_priority_queue.insert('C', 7)
max_priority_queue.insert('X', 10)
max_priority_queue.insert('Y', 8)
max_priority_queue.insert('Z', 12)

# Peek and delete operations
print("Min Priority Queue:")
print(min_priority_queue.peek())  # Should print 'B' (highest priority)
print(min_priority_queue.delete())  # Should print 'B' (highest priority)
print(min_priority_queue.delete())  # Should print 'A'
print(min_priority_queue.peek())  # Should print 'C' (highest priority)

print("\nMax Priority Queue:")
print(max_priority_queue.peek())  # Should print 'Z' (highest priority)
print(max_priority_queue.delete())  # Should print 'Z' (highest priority)
print(max_priority_queue.delete())  # Should print 'X'
print(max_priority_queue.peek())  # Should print 'Y' (highest priority)

# Changing priority
min_priority_queue.changePriority('C', 1)
print("Changed Priority in Min Priority Queue:")
print(min_priority_queue.peek())  # Should print 'C' (highest priority)

max_priority_queue.changePriority('Y', 15)
print("\nChanged Priority in Max Priority Queue:")
print(max_priority_queue.peek())  # Should print 'Y' (highest priority)

