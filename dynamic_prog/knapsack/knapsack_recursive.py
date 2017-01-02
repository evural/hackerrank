import sys
RECURSION_LIMIT = 3000
sys.setrecursionlimit(RECURSION_LIMIT)
# Recursive solution
def knapsack(items, knapsack_arr, capacity, i=0):
    if i == len(items) or capacity < 0:
        return 0
    if knapsack_arr[i][capacity] > 0:
        return knapsack_arr[i][capacity]
    if items[i] <= capacity:
        knapsack_arr[i][capacity] = max(items[i] + knapsack(items, knapsack_arr, capacity-items[i], i), knapsack(items, knapsack_arr, capacity, i+1))
    else:
        knapsack_arr[i][capacity] = knapsack(items, knapsack_arr, capacity, i+1)
    return knapsack_arr[i][capacity]


if __name__ == "__main__":
    number_of_tests = int(raw_input())
    for i in range(0, number_of_tests):
        line = raw_input()
        number_of_elems, expected_sum = (int(n) for n in line.split())
        line = raw_input()
        items = [int(n) for n in line.split()]
        knapsack_arr = [[0 for i in range(expected_sum+1)] for j in range(len(items))]
        print knapsack(items, knapsack_arr, expected_sum)
