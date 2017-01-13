import sys
sys.path.append('/home/ersan/Desktop/algorithm/hackerrank/cracking/data_structures')
from linked_list import LinkedList, Node

def remove_node(node):
    node.data = node.next.data
    node.next = node.next.next

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
    node = linked_list.head
    for i in range(0, 3):
        node = node.next
    remove_node(node)
    print linked_list

