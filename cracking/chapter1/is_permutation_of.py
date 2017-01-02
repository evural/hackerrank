def is_permutation_of(str1, str2):
    if len(str1) != len(str2):
        return False
    hash_table = {}
    for c in str1:
        if c in hash_table:
            hash_table[c] += 1
        else:
            hash_table[c] = 1
    for c in str2:
        if c not in hash_table:
            return False
        hash_table[c] -= 1
    for key in hash_table:
        if hash_table[key] != 0:
            return False
    return True

if __name__ == "__main__":
    str1, str2 = raw_input().split()
    print is_permutation_of(str1, str2)
