
# Returns true if all characters of text are unique, returns false otherwise
# Put all characters to a hash table (k,v) -> (character, count)
# If hash table key was inserted before, return false
def is_unique(text):
    # Since there are at most 128 unique characters, if text length is greater than 128, text cannot have all unique characters
    if len(text) > 128:
        return false
    hash_table = {}
    for c in text:
        char_ascii = ord(c)
        if char_ascii < 0 and char_ascii > 128:
            return False
        if char_ascii in hash_table:
            return False
        hash_table[char_ascii] = 1
    return True


if __name__ == "__main__":
    text = raw_input()
    print is_unique(text)
