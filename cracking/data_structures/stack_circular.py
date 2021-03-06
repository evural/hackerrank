class EmptyStackError(Exception):
    def __init__(self, message, errors = None):
        super(EmptyStackError, self).__init__(message)

class FullStackError(Exception):
    def __init__(self, message, errors = None):
        super(FullStackError, self).__init__(message)

class Node:
    def __init__(self, data):
        self.data = data

class Stack:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.top = -1
        self.bottom = 0
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size >= self.capacity
    def get_size(self):
        return self.size
    def push(self, data):
        if self.is_full():
            raise FullStackError("Stack is full")
        node = Node(data)
        self.top = (self.top + 1) % self.capacity
        self.size += 1
        self.arr[self.top] = node 
    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        node = self.arr[self.top]
        self.top = (self.top - 1) % self.capacity
        self.size -= 1
        return node.data
    def remove_bottom(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        node = self.arr[self.bottom]
        self.bottom = (self.bottom + 1) % self.capacity
        self.size -= 1
        return node.data
    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        node = self.arr[self.top]
        return node.data
    def __str__(self):
        if self.size == 0:
            return ""
        return_arr = []
        if self.bottom <= self.top:
            l_index = self.bottom
            r_index = (self.top + 1) % (self.capacity+1)
            return_arr = self.arr[l_index:r_index]
        else:
            l_index = (self.bottom + 1) % (self.capacity+1)
            r_index = self.top
            return_arr = self.arr[r_index:self.capacity] + self.arr[0:l_index]
        data_values = [str(x.data) for x in return_arr]
        return " ".join(data_values)


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
    print stack.pop()
