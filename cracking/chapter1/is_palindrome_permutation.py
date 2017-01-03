# Check if the string contains characters even number of times

def is_palindrome_permutation(text):
    text = text.replace(" ", "")
    text = text.lower()
    hash_table = {}
    for c in text:
        if c in hash_table:
            hash_table[c] += 1
        else:
            hash_table[c] = 1
    odd_count = 0
    for key in hash_table:
        if hash_table[key] % 2 == 1:
            odd_count += 1
    if len(text) % 2 == 0 and odd_count > 0:
        return False
    if len(text) % 2 == 1 and odd_count > 1:
        return False
    return True


if __name__ == "__main__":
    text = raw_input()
    print is_palindrome_permutation(text)
