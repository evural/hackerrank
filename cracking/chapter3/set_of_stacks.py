import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from stack import Stack

class SetofStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity
    def push(self, data):
        if self.stacks == [] or self.stacks[len(self.stacks) - 1].is_full():
            new_stack = Stack(self.capacity)
            self.stacks.append(new_stack)
        self.stacks[len(self.stacks) - 1].push(data)
    def pop(self):
        if self.stacks == []:
            return None
        data = self.stacks[len(self.stacks) - 1].pop()
        if self.stacks[len(self.stacks) - 1].is_empty():
            del self.stacks[len(self.stacks) - 1]
        return data
    def peek(self):
        if self.stacks == []:
            return None
        return self.stacks[len(self.stacks) - 1].peek()

if __name__ == "__main__":
    stack = SetofStacks(2)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)
    stack.push(4)
    stack.pop()
    stack.pop()
    print len(stack.stacks)
    print stack.peek()
