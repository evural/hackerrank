
def is_rotation(str1, str2):
    str1_list = []
    for c in str1:
        str1_list.append(c)
    for c in str1:
        str1_list.append(c)
    str1 = "".join(str1_list)
    if str2 in str1:
        return True
    return False


if __name__ == "__main__":
    str1 = raw_input()
    str2 = raw_input()
    print is_rotation(str1, str2)
