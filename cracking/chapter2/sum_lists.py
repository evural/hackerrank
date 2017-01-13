import sys
sys.path.append('/home/ersan/Desktop/algorithm/hackerrank/cracking/data_structures')
from linked_list import LinkedList

def list2int(arr, base):
    result_sum = 0
    digit = 1
    for i in range(0, len(arr)):
        result_sum += (arr[i] * digit)
        digit *= base
    return result_sum


def sum_lists(list1, list2, base):
    result_list = [] 
    node1 = list1.head
    node2 = list2.head
    remainder = 0
    current_sum = 0
    while(node1 != None or node2 != None):
        if node1 == None:
            current_sum = node2.data + remainder
            node2 = node2.next
        elif node2 == None:
            current_sum = node1.data + remainder
            node1 = node1.next
        else:
            current_sum = node1.data + node2.data + remainder
            node1 = node1.next
            node2 = node2.next

        if current_sum >= base:
            remainder = current_sum / base
            current_sum = current_sum % base
        else:
            remainder = 0
        result_list.append(current_sum)

    if remainder != 0:
        result_list.append(remainder)
    return list2int(result_list, base)


if __name__ == "__main__":
    linked_list1 = LinkedList()
    linked_list1.insert_back(5)
    linked_list1.insert_back(6)
    linked_list1.insert_back(7)
    linked_list2 = LinkedList()
    linked_list2.insert_back(8)
    linked_list2.insert_back(9)
    linked_list2.insert_back(9)
    print linked_list1
    print linked_list2
    print sum_lists(linked_list1, linked_list2, 10)
