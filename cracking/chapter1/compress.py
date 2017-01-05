
def compress(text):
    if len(text) < 2:
        return text
    compressed_text = [] 
    previous_char = text[0]
    count = 1
    for i in range(1, len(text)):
        c = text[i]
        if c == previous_char:
            count += 1
            continue
        compressed_text.append(previous_char)
        compressed_text.append(`count`)
        previous_char = c
        count = 1
    compressed_text.append(previous_char)
    compressed_text.append(`count`)
    if len(compressed_text) < len(text):
        return "".join(compressed_text)
    return text
    

if __name__ == "__main__":
    text = raw_input()
    print compress(text)
