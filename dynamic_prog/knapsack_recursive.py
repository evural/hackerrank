import sys
sys.setrecursionlimit(3000)
# Recursive solution
def knapsack(items, capacity,i=0):
    if i == len(items):
        return 0
    if items[i] <= capacity:
        return max(items[i] + knapsack(items, capacity-items[i], i), knapsack(items, capacity, i+1))
    else:
        return knapsack(items, capacity,i+1)


if __name__ == "__main__":
    number_of_tests = int(raw_input())
    for i in range(0, number_of_tests):
        line = raw_input()
        number_of_elems, expected_sum = (int(n) for n in line.split())
        line = raw_input()
        items = [int(n) for n in line.split()]
        print knapsack(items, expected_sum)
