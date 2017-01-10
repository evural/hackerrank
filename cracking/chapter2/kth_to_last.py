# Basic implementation
# N time to get size, N time to find the node: Total of 2N time

import sys
sys.path.append('/home/ersan/Desktop/algorithm/hackerrank/cracking/data_structures')
from linked_list import LinkedList

def kth_to_last(linked_list, k):
    size = linked_list.get_size()
    if k > size:
        return None
    index = size - k
    node = linked_list.head
    i = 0
    while(node != None):
        if i == index:
            return node
        i += 1
        node = node.next
    return node


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_front(1)
    linked_list.insert_front(2)
    linked_list.insert_front(3)
    linked_list.insert_front(0)
    linked_list.insert_front(5)
    linked_list.insert_front(2)
    linked_list.insert_front(6)
    linked_list.insert_front(5)
    linked_list.insert_front(3)
    print linked_list
    node = kth_to_last(linked_list, 9)
    if node == None:
        print None
    else:
        print node.data
