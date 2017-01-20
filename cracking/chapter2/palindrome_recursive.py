import sys
sys.path.append('/home/ersan/Desktop/algorithms/hackerrank/cracking/data_structures')
from linked_list import LinkedList
from stack import Stack

def palindrome(linked_list):
    length = linked_list.get_size()
    node = linked_list.head
    return palindrome_helper(node, length)
    
def palindrome_helper(node, size):
    if size == 0:
        return True, node
    if size == 1:
        return True, node.next
    is_palindrome, corr_node = palindrome_helper(node.next, size-2)
    if is_palindrome == False:
        return False, corr_node.next
    if corr_node.data == node.data:
        return True, corr_node.next
    return False, corr_node.next

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_back("k")
    linked_list.insert_back("a")
    linked_list.insert_back("b")
    linked_list.insert_back("b")
    linked_list.insert_back("a")
    linked_list.insert_back("k")
    print linked_list
    print palindrome(linked_list)
