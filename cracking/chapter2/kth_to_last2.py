# Implementation with fast pointer
# Max O(N) time

import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from linked_list import LinkedList



def kth_to_last(linked_list, k):
    i = 0
    r_node = linked_list.head
    while(r_node != None and i < k):
        r_node = r_node.next
        i += 1
    if i != k:
        return None
    l_node = linked_list.head
    while(r_node != None):
        l_node = l_node.next
        r_node = r_node.next
    return l_node


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
    node = kth_to_last(linked_list, 10)
    if node == None:
        print None
    else:
        print node.data
                      

