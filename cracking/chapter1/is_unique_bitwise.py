# 1. Initialize a checker variable to 0
# 2. For each character in the text, shift left bits of 1
# 3. If bitwise AND of this value returns a number other than 0, return False
# 4. Bitwise OR this value with the checker variable

def is_unique(text):
    checker = 0
    for c in text:
        val = ord(c) - ord("a")
        shifted = 1 << val
        if checker & shifted != 0:
            return False
        checker = checker | shifted 
    return True

if __name__ == "__main__":
    text = raw_input()
    print is_unique(text)
