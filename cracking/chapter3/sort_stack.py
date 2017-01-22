import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from stack_circular import Stack

def sort_stack(stack):
    stack_size = stack.get_size()
    tmp_stack = Stack(stack_size)
    for i in range(0, stack_size):
        max = float("-inf")
        for j in range(0, stack_size - i):
            value = stack.pop()
            tmp_stack.push(value)
            if value > max:
                max = value
        stack.push(max)
        is_passed = False
        while(tmp_stack.is_empty() == False):
            value = tmp_stack.pop()
            # Check if same values exist in order not to pass value multiple times
            if value == max and is_passed == False:
                is_passed = True
                continue
            stack.push(value)

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
