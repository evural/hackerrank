# Hash table implementation
# O(N) time
# O(N) space

import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from linked_list import LinkedList


def remove_dups(linked_list):
    if linked_list.head == None:
        return
    hash_table = {}
    node = linked_list.head
    hash_table[node.data] = 1
    while(node.next != None):
        if node.next.data in hash_table:
            node.next = node.next.next
        else:
            hash_table[node.next.data] = 1
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

