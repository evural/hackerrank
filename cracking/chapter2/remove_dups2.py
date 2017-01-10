# Iteration implementation
# O(N^2) time
# O(1) space

import sys
sys.path.append('/home/ersan/Desktop/algorithm/hackerrank/cracking/data_structures')
from linked_list import LinkedList


def remove_dups(linked_list):
    if linked_list.head == None:
        return
    node = linked_list.head
    while(node != None):
        iterator_node = node
        while(iterator_node.next != None):
            if iterator_node.next.data == node.data:
                iterator_node.next = iterator_node.next.next
            else: 
                iterator_node = iterator_node.next
        node = node.next

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
    remove_dups(linked_list)
    print linked_list

