# O(N^2) time complexity
# O(M+N) space complexity. We can do better in terms of space complexity!!!

import sys
def set_zero(matrix):
    if len(matrix) == 0:
        return
    h_list = [0] * len(matrix)
    v_list = [0] * len(matrix[0])

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0:
                h_list[i] = 1
                v_list[j] = 1

    for i in range(0, len(h_list)):
        if h_list[i] == 1:
            matrix[i] = [0] * len(matrix[i])
    for j in range(0, len(v_list)):
        if v_list[j] == 1:
            for i in range(0, len(matrix)):
                matrix[i][j] = 0

def print_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            sys.stdout.write(str(matrix[i][j]) + " ")
        sys.stdout.write("\n")

if __name__ == "__main__":
    matrix = [[1,2,3],[4,0,6],[7,8,9], [5,8,0]]
    print_matrix(matrix)
    set_zero(matrix)
    print "============"
    print_matrix(matrix)
