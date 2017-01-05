# O(N^2) time complexity
# O(1) space complexity, using first row and first column as the zero tracker arrays

import sys

def set_zero(matrix):
    if len(matrix) == 0:
        return
    row_has_zero = False
    column_has_zero = False

    # Check if first row has zero
    for j in range(0, len(matrix[0])):
        if matrix[0][j] == 0:
            row_has_zero = True
    # Check if first column has zero
    for i in range(0, len(matrix)):
        if matrix[i][0] == 0:
            column_has_zero = True
    # Populate zeros to first row and column
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    # Check zeros in first row
    for j in range(0, len(matrix[0])):
        if matrix[0][j] == 0:
            nullify_column(matrix, j)
    # Check zeros in first column
    for i in range(0, len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)
    # Nullify first fow
    if row_has_zero:
        nullify_row(matrix, 0)
    # Nullify first column
    if column_has_zero:
        nullify_column(matrix, 0)

def nullify_row(matrix, row):
    for j in range(0, len(matrix[0])):
        matrix[row][j] = 0

def nullify_column(matrix, column):
    for i in range(0, len(matrix)):
        matrix[i][column] = 0

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
