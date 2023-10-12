class PriorityQueue:
    def __init__(self, is_max_heap=False):
        self.elements = []
        self.is_max_heap = is_max_heap

    def insert(self, item, priorityValue):
        self.elements.append((item, priorityValue))
        self._heapify_up(len(self.elements) - 1)

    def _heapify_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if (self.elements[idx][1] > self.elements[parent_idx][1]) if self.is_max_heap else (self.elements[idx][1] < self.elements[parent_idx][1]):
                self.elements[idx], self.elements[parent_idx] = self.elements[parent_idx], self.elements[idx]
                idx = parent_idx
            else:
                break

    def peek(self):
        if not self.elements:
            return None
        return self.elements[0][0]

    def delete(self):
        if not self.elements:
            return None
        if len(self.elements) == 1:
            return self.elements.pop()[0]
        root = self.elements[0][0]
        self.elements[0] = self.elements.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, idx):
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            largest = idx

            if left_child_idx < len(self.elements) and ((self.elements[left_child_idx][1] > self.elements[largest][1]) if self.is_max_heap else (self.elements[left_child_idx][1] < self.elements[largest][1])):
                largest = left_child_idx

            if right_child_idx < len(self.elements) and ((self.elements[right_child_idx][1] > self.elements[largest][1]) if self.is_max_heap else (self.elements[right_child_idx][1] < self.elements[largest][1])):
                largest = right_child_idx

            if largest != idx:
                self.elements[idx], self.elements[largest] = self.elements[largest], self.elements[idx]
                idx = largest
            else:
                break

    def changePriority(self, item, newPriority):
        for i in range(len(self.elements)):
            if self.elements[i][0] == item:
                old_priority = self.elements[i][1]
                self.elements[i] = (item, newPriority)
                if (newPriority > old_priority) if self.is_max_heap else (newPriority < old_priority):
                    self._heapify_down(i)
                else:
                    self._heapify_up(i)

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

