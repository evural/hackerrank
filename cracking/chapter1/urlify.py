# Iterate over the string starting from the end to use the extra buffer at the end
# If there is a space, replace with %20; otherwise copy the original character

def urlify(text, real_size):
    if len(text) == real_size:
        return text
    j = len(text) - 1
    for i in range(real_size-1, -1, -1):
        if text[i] != " ":
            text = swap(text, i, j)
            j -= 1
        else:
            text[j-2:j+1] = "%20"
            j -= 3
    return "".join(text)

def swap(text, index1, index2):
    c = text[index1]
    text[index1] = text[index2]
    text[index2] = c
    return text

if __name__ == "__main__":
    real_size = int(raw_input())
    text = raw_input()
    print text
    l_text = list(text)
    print urlify(l_text, real_size)
