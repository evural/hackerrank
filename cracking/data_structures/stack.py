class EmptyStackError(Exception):
    def __init__(self, message, errors = None):
        super(EmptyStackError, self).__init__(message)

class FullStackError(Exception):
    def __init__(self, message, errors = None):
        super(FullStackError, self).__init__(message)

class Stack:
    def __init__(self, max_size=0):
        self.arr = []
        self.max_size = max_size

    def is_empty(self):
        if self.len() == 0:
            return True
        return False

    def is_full(self):
        if self.len() >= self.max_size:
            return True
        return False

    def len(self):
        return len(self.arr)

    def push(self, element):
        if self.is_full():
            raise FullStackError("Stack is full: cannot push to a full stack")
        else:
            self.arr.append(element)
        return self.arr 

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty: cannot pop from an empty stack!")
            return None
        elem = self.arr[len(self.arr) - 1]
        del self.arr[len(self.arr) - 1]
        return elem

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty: cannot peek from empty stack!")
            return None
        return self.arr[0]
        
        
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
