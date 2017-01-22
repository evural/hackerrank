import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from stack_circular import Stack

def sort_stack(stack):
    stack_size = stack.get_size()
    tmp_stack = Stack(stack_size)
    while(stack.is_empty() == False):
        value = stack.pop()
        if tmp_stack.is_empty() or tmp_stack.peek() <= value:
            tmp_stack.push(value)
        else:
            while(tmp_stack.is_empty() == False):
                stack.push(tmp_stack.pop())
            stack.push(value)
    while(tmp_stack.is_empty() == False):
        stack.push(tmp_stack.pop())

if __name__ == "__main__":
    stack = Stack(10)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(12)
    stack.push(5)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    print stack 
    sort_stack(stack)
    print stack
