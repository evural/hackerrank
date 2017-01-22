import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from stack_circular import Stack

class FullQueueError(Exception):
    def __init__(self, message, errors = None):
        super(FullStackError, self).__init__(message)

class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = Stack(capacity)
        self.reverse_stack = Stack(capacity)
    def is_full(self):
        return self.stack.get_size() + self.reverse_stack.get_size() >= self.capacity
    def enqueue(self, data):
        if self.is_full():
            raise FullQueueError("Queue is full")
        self.stack.push(data)
    def dequeue(self):
        if self.reverse_stack.is_empty():
            while(self.stack.is_empty() == False):
                self.reverse_stack.push(self.stack.pop())
        return self.reverse_stack.pop()
         
if __name__ == "__main__":
    queue = MyQueue(15)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    value = queue.dequeue()
    print value
