import sys

# Number of subproblems = n*S where n = number_of_elems and S = expected_sum
# Guess: Should I take the kth item. # = 2(Yes/No) 
# Basic approach w/o considering capacity:  result[i] = max(result[i+1], result[i+1] + items[i])
# Approach: result[i][j] = max(result[i+1][j], items[i] + result[i+1][j-items[i]])
# Since an item can be taken multiple times: result[i][j] = max(result[i+1][j], items[i] + result[i][j-items[i]])

def knapsack(items, capacity):
    # Result table: (len(items)+1)x(capacity+1)
    # result[len(items)] values are set to 0 as initial condition
    result = [[0 for i in range(capacity+1)] for j in range(len(items)+1)]
    for i in range(len(items)-1, -1, -1):
        for j in range(0, capacity+1):
            if items[i] <= j:
                result[i][j] = max(result[i+1][j], items[i] + result[i][j-items[i]])
            else:
                result[i][j] = result[i+1][j]
    return result[0][capacity]



if __name__ == "__main__":
    number_of_tests = int(raw_input())
    for i in range(0, number_of_tests):
        line = raw_input()
        number_of_elems, expected_sum = (int(n) for n in line.split())
        line = raw_input()
        items = [int(n) for n in line.split()]
        print knapsack(items, expected_sum)
