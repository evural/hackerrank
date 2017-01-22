import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get_size(self):
        node = self.head
        i = 0
        while(node != None):
            node = node.next
            i += 1
        return i

    def get_node_at(self, index):
        i = 0
        node = self.head
        while(node != None and i < index):
            node = node.next
            i += 1
        return node

    def get_last_node(self):
        node = self.head
        while(node != None and node.next != None):
            node = node.next
        return node
    
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node   

    def insert_back(self, data):
        if self.get_size() == 0:
            return self.insert_front(data)
        new_node = Node(data)
        last_node = self.get_last_node()
        last_node.next = new_node

    def insert_at(self, data, index):
        if index == 0:
            return self.insert_front(data)
        new_node = Node(data)
        prev_node = self.get_node_at(index-1)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def remove_front(self):
        if self.get_size() == 0:
            return
        self.head = self.head.next

    def remove_back(self):
        size = self.get_size()
        if size == 0:
            return
        prev_node = self.get_node_at(size-2)
        prev_node.next = None

    def remove_at(self, index):
        prev_node = self.get_node_at(index-1)
        if prev_node == None or prev_node.next == None:
            return
        prev_node.next = prev_node.next.next

    def find(self, data):
        node = self.head
        i = 0
        while(node != None):
            if node.data == data:
                return i
            node = node.next
            i += 1
        return -1

    def __str__(self):
        node = self.head
        while(node != None):
            sys.stdout.write(str(node.data) + " ")
            node = node.next
        return ""

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_front(1)
    print linked_list.get_node_at(0).data
