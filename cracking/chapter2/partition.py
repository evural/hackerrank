import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from linked_list import LinkedList


def partition(linked_list, pivot):
    if linked_list.head == None:
        return

    index_node = None
    if linked_list.head.data < pivot:
        index_node = linked_list.head
    iterator = linked_list.head
    while(iterator.next != None):
        if iterator.next.data < pivot:
            l_node = iterator.next
            if index_node == None:
                iterator.next = iterator.next.next
                l_node.next = linked_list.head
                linked_list.head = l_node
            else:
                iterator.next = iterator.next.next
                l_node.next = index_node.next
                index_node.next = l_node
            index_node = l_node
        else:
            iterator = iterator.next 


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_back(3)
    linked_list.insert_back(5)
    linked_list.insert_back(8)
    linked_list.insert_back(5)
    linked_list.insert_back(10)
    linked_list.insert_back(2)
    linked_list.insert_back(1)
    print linked_list
    partition(linked_list, 5)
    print linked_list
