import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from stack import Stack

class MinStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.actual_stack = Stack(capacity)
        self.min_stack = Stack(capacity)

    def push(self, data):
        self.actual_stack.push(data)
        if self.min_stack.is_empty() or data <= self.min_stack.peek():
            self.min_stack.push(data)
    def pop(self):
        data = self.actual_stack.pop()
        if data == self.min_stack.peek():
            self.min_stack.pop()
        return data
    def min(self):
        return self.min_stack.peek()
    

if __name__ == "__main__":
    stack = MinStack(15)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)
    stack.push(4)
    stack.pop()
    print stack.min()
