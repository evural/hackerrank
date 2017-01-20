import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from linked_list import LinkedList


def intersection(linked_list1, linked_list2):
    size1 = linked_list1.get_size()
    size2 = linked_list2.get_size()
    node1 = linked_list1.head
    node2 = linked_list2.head
    if size1 > size2:
        for i in range(0, size1-size2):
            node1 = node1.next
    if size2 > size1:
        for i in range(0, size2-size1):
            node2 = node2.next

    while(node1 != None and node2 != None):
        if node1 == node2:
            return node1.data
        node1 = node1.next
        node2 = node2.next
    return None


if __name__ == "__main__":
    linked_list1 = LinkedList()
    linked_list1.insert_front(1)
    linked_list1.insert_front(2)
    linked_list1.insert_front(3)
    linked_list1.insert_front(0)
    linked_list1.insert_front(5)
    linked_list1.insert_front(2)
    linked_list1.insert_front(6)
    linked_list1.insert_front(5)
    linked_list1.insert_front(3)
    linked_list2 = LinkedList()
    node = linked_list1.head
    node2 = node.next.next.next.next
    linked_list2.head = node2
    print intersection(linked_list1, linked_list2)
