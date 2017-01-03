
def is_palindrome_permutation(text):
    text = text.replace(" ", "")
    text = text.lower()
    checker = 0
    for c in text:
        value = ord(c) - ord("a")
        shifted = 1 << value
        checker ^= shifted
    if len(text) % 2 == 0 and checker == 0:
        return True
    if len(text) % 2 == 1 and check_exactly_one_bit_set(checker):
        return True
    return False

def check_exactly_one_bit_set(nmbr):
    return (nmbr & (nmbr - 1)) == 0

if __name__ == "__main__":
    text = raw_input()
    print is_palindrome_permutation(text)
