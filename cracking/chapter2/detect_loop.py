import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from linked_list import LinkedList

def detect_loop(linked_list):
    if linked_list.head == None:
        return None
    node = linked_list.head
    runner_node = linked_list.head
    while(runner_node != None and runner_node.next != None):
        node = node.next
        runner_node = runner_node.next.next
        if node == runner_node:
            break
    if node != runner_node:
        return None
    node = linked_list.head
    while(node != None and runner_node != None):
        if node == runner_node:
            return node.data
        node = node.next
        runner_node = runner_node.next
    return None


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
    node = linked_list.head
    node2 = node.next.next.next.next.next
    while(node.next != None):
        node = node.next
    node.next = node2
    print node2.data
    print detect_loop(linked_list)
