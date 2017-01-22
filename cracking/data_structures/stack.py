class EmptyStackError(Exception):
    def __init__(self, message, errors = None):
        super(EmptyStackError, self).__init__(message)

class FullStackError(Exception):
    def __init__(self, message, errors = None):
        super(FullStackError, self).__init__(message)

class Stack:
    def __init__(self, capacity=0):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.top = -1
        self.size = 0

    def is_empty(self):
        return self.get_size() == 0

    def is_full(self):
        return self.get_size() >= self.capacity

    def get_size(self):
        return self.size

    def push(self, element):
        if self.is_full():
            raise FullStackError("Stack is full: cannot push to a full stack")
        self.top += 1
        self.arr[self.top] = element
        self.size += 1
        return self.arr 

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty: cannot pop from an empty stack!")
        elem = self.arr[self.top]
        self.top -= 1
        self.size -= 1
        return elem

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty: cannot peek from empty stack!")
            return None
        return self.arr[self.top]
        
        
if __name__ == "__main__":
    stack = Stack(15)
    #value = stack.pop()
    stack.push(1)
    value = stack.pop()
    print value
    #value = stack.pop()
    #print value
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    value = stack.pop()
    print value
    print stack.peek()
