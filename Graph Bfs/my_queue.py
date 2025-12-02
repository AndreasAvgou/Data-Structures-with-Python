# Filename: my_queue.py
from array import array

class GraphQueue:
    def __init__(self, capacity):
        # Initialize queue array and pointers
        self.size = capacity
        self.queue = array('i', [0] * capacity)
        self.front = -1
        self.rear = -1

    def enqueue(self, k):
        f = 0
        if self.front == -1:
            self.front = 0
        
        if self.rear < self.size - 1:
            self.rear = self.rear + 1
            self.queue[self.rear] = k
            f = 1
        return f

    def dequeue(self):
        f = 0
        k = 0
        if self.front != -1:
            k = self.queue[self.front]
            self.front = self.front + 1
            f = 1
            
        # Reset pointers if queue becomes empty
        if self.front > self.rear:
            self.rear = -1
            self.front = -1
            
        return k, f