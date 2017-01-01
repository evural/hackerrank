import sys
# To solve the text justification problem: 
# for each word, suppose a line starts with that word, and find out where the next line should start
# Example: text ="Tushar Roy likes to code", width=10
# First line starts with Tushar, what about 2nd line? Try all remainin words as the start of 2nd line, and get the min
# 5: "Tushar Roy likes to code" = Either "Tushar" + "Roy likes to code", or "Tushar Roy" + "likes to code"
# 4: "Roy likes to code" = Either "Roy" + "likes to code", or "Roy likes" + "to code"
# 3: "likes to code" = Either "likes" + "to code", or "likes to" + "code" 
# 2: "to code" = min((10-7)^3, (10-2)^3 + baddness("code")
# 1: "code" = (10-4)^3
# Time complexity: n^2
# Space complexity: n

# We are trying the minimize the overall badness value
def calc_badness(width, size):
    return (width-size)*(width-size)*(width-size)

def text_justification(text, width):
    word_list = text.split()
    # Result array keeps track of the word which starts the next line.
    result_arr = [0 for x in range(0, len(word_list))]
    # Each word has a badness value, which is the badness value of string starting from the corresponding word
    badness_list = [float("inf") for x in range(0, len(word_list)+1)]
    tj(word_list, width, result_arr, badness_list, 0)

def tj(word_list, width, result_arr, badness_list, i):
    # Base case:
    if len(word_list) == i:
        return 0
    # Phrase size is initialized to -1 because a line does not start with space 
    phrase_size = -1
    for j in range(i+1, len(word_list) + 1):
        # +1 is for the space between words
        phrase_size += len(word_list[j-1]) + 1
        if  phrase_size <= width:
            badness = calc_badness(width, phrase_size)
            if badness_list[j] == float("inf"):
                badness += tj(word_list, width, result_arr, badness_list, j)
            else:
                badness += badness_list[j]
            if badness < badness_list[i]:
                badness_list[i] = badness
                result_arr[i] = j
    # if i == 0, then the recursion is completed, print the result
    if i == 0:
        print_result(word_list, result_arr)
    return badness_list[i] 

def print_result(word_list, result_arr):
    prev_value = 0
    while(len(result_arr) > 0):
        value = result_arr[0] - prev_value
        prev_value = result_arr[0]
        for i in range(value):
            sys.stdout.write(word_list[i] + " ")
        sys.stdout.write("\n")
        result_arr = result_arr[value:]
        word_list = word_list[value:]

if __name__ == "__main__":
    width = int(raw_input())
    text = raw_input() 
    text_justification(text, width)
