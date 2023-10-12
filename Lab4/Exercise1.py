class MinPQ:

    def __init__(self):
        self.pq = []

    def insert(self, item, priority):
        self.pq.append((priority, item))
        self.pq.sort()

    def peek(self):
        return self.pq[0][1]
    
    def pop(self):
        return self.pq.pop(0)[1]

class MaxPQ:

    def __init__(self):
        self.pq = []

    def insert(self, item, priority):
        self.pq.append((-priority, item))
        self.pq.sort()

    def peek(self):
        return self.pq[0][1]

    def pop(self):
        return self.pq.pop(0)[1]

minpq = MinPQ()
minpq.insert('A', 3) 
minpq.insert('B', 1)
minpq.insert('C', 2)

print(minpq.pop()) # B

maxpq = MaxPQ() 
maxpq.insert('A', 3)
maxpq.insert('B', 1) 
maxpq.insert('C', 2)

print(maxpq.pop()) # A
