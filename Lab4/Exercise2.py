class Node:
    def __init__(self, item, priorityValue):
        self.item = item
        self.priorityValue = priorityValue
        self.next = None

class PriorityQueue:
    def __init__(self, is_max_heap=False):
        self.head = None
        self.is_max_heap = is_max_heap

    def insert(self, item, priorityValue):
        new_node = Node(item, priorityValue)
        if not self.head:
            self.head = new_node
        else:
            if (priorityValue > self.head.priorityValue) if self.is_max_heap else (priorityValue < self.head.priorityValue):
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                while current.next and ((priorityValue <= current.next.priorityValue) if self.is_max_heap else (priorityValue >= current.next.priorityValue)):
                    current = current.next
                new_node.next = current.next
                current.next = new_node

    def peek(self):
        if not self.head:
            return None
        return self.head.item

    def delete(self):
        if not self.head:
            return None
        item = self.head.item
        self.head = self.head.next
        return item

    def changePriority(self, item, newPriority):
        if not self.head:
            return
        if (newPriority > self.head.priorityValue) if self.is_max_heap else (newPriority < self.head.priorityValue):
            return
        if self.head.item == item:
            self.head.priorityValue = newPriority
            return
        current = self.head
        while current.next and current.next.item != item:
            current = current.next
        if current.next:
            current.next.priorityValue = newPriority
            current = self.head
            while current.next and ((newPriority <= current.next.priorityValue) if self.is_max_heap else (newPriority >= current.next.priorityValue)):
                current = current.next
            if current.next != current:
                temp = current.next
                current.next = temp.next
                temp.next = self.head
                self.head = temp

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

