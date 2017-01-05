
def compress(text):
    if len(text) < 2:
        return text
    new_text = [] 
    previous_char = text[0]
    count = 1
    for i in range(1, len(text)):
        c = text[i]
        if c == previous_char:
            count += 1
            continue
        new_text.append(previous_char)
        new_text.append(`count`)
        previous_char = c
        count = 1
    new_text.append(previous_char)
    new_text.append(`count`)
    if len(new_text) < len(text):
        return "".join(new_text)
    return text
    

if __name__ == "__main__":
    text = raw_input()
    print compress(text)
