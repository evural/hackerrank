
def is_one_edit_distance(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    if len(str2) < len(str1):
        str1, str2 = str2, str1
    distance = False
    index1 = 0
    index2 = 0
    for i in range(0, len(str2)):
        if index1 >= len(str1) or str1[index1] != str2[index2]:
            if distance:
                return False
            distance = True
            index2 += 1
            if len(str1) == len(str2):
                index1 += 1
        else:
            index1 += 1
            index2 += 1
    return True


if __name__ == "__main__":
    str1 = raw_input()
    str2 = raw_input()
    print is_one_edit_distance(str1, str2)
    
    
