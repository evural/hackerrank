import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from linked_list import LinkedList


def partition(linked_list, pivot):
    if linked_list.head == None:
        return

    result_list = LinkedList()
    iterator = linked_list.head
    while(iterator != None):
        if iterator.data < pivot:
            result_list.insert_front(iterator.data)
        else:
            result_list.insert_back(iterator.data)
        iterator = iterator.next 
    return result_list

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
    result_list = partition(linked_list, 5)
    print result_list
