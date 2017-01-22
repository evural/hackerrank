import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from stack_circular import Stack

class SetofStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity
    def get_last_stack(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[-1]
    def push(self, data):
        last_stack = self.get_last_stack()
        if last_stack == None or last_stack.is_full() == True:
            new_stack = Stack(self.capacity)
            self.stacks.append(new_stack)
            last_stack = new_stack
        last_stack.push(data)
    def pop(self):
        last_stack = self.get_last_stack()
        if last_stack == None:
            return None
        data = last_stack.pop()
        if last_stack.is_empty():
            del self.stacks[-1]
        return data
    def pop_at(self, index):
        if index < 0 or index >= len(self.stacks):
            return None
        data = self.stacks[index].pop()
        self.shift(index)
        return data
    def shift(self, index):
        if index < 0 or index >= len(self.stacks) - 1:
            if self.stacks[index].is_empty():
                del self.stacks[index]
            return
        data_shift = self.stacks[index+1].remove_bottom()
        self.stacks[index].push(data_shift)
        self.shift(index+1)
    def peek(self):
        last_stack = self.get_last_stack()
        if last_stack == None:
            return None
        return last_stack.peek()

if __name__ == "__main__":
    stack = SetofStacks(2)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)
    stack.push(4)
    stack.pop_at(2)
    stack.pop_at(2)
    stack.pop_at(0)
    stack.pop_at(0)
    stack.pop()
    print len(stack.stacks)
    print stack.peek()
