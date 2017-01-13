
class SumHelper:
    def __init__(self, sum=0, rem=0):
        self.sum = sum
        self.rem = rem

def sum_lists(list1, list2):
    size1 = list1.get_size()
    size2 = list2.get_size()
    if size1 < size2:
        pad_list(list1, size2 - size1)
    elif size2 < size1:
        pad_list(list2, size1 - size2)
  
    sum_helper(list1.head, list2.head)

def sum_helper(node1, node2):
    if list1 == None and list2 == None:
        return SumHelper()
    next_sum = sum_helper(node1.next, node2.next)
    current_sum = node1.data + node2.data + next_sum.rem
    current_rem = 0
    if current_sum >= 10:
        current_rem = current_sum / 10
        current_sum = current_sum % 10
    return SumHelper(current_sum, current_rem)
    

def pad_list(linked_list, pad_len):
    for i in range(0, len(pad_len)): 
        linked_list.insert_front(0)
