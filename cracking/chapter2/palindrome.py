import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from linked_list import LinkedList
from stack import Stack


def palindrome(linked_list):
    length = linked_list.get_size()
    mid_index = length / 2
    node = linked_list.head
    i = 0
    stack = Stack(length/2)
    while(node != None):
        if i < mid_index:
            stack.push(node.data)
        elif i > mid_index:
            if stack.pop() != node.data:
                return False
        elif length % 2 == 0:
            if stack.pop() != node.data:
                return False
        node = node.next
        i += 1
    return True
    

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_back("t")
    linked_list.insert_back("a")
    linked_list.insert_back("b")
    linked_list.insert_back("t")
    print linked_list
    print palindrome(linked_list)
