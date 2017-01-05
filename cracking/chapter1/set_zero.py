import sys
def set_zero(matrix):
    h_list = []
    v_list = []

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0:
                h_list.append(i)
                v_list.append(j)

    for i in range(0, len(h_list)):
        matrix[i] = [0] * len(matrix)
    #for j in range(0, len(v_list)):
    #    for i in range(0, len(matrix)):
    #        matrix[i][j] = 0

def print_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            sys.stdout.write(str(matrix[i][j]) + " ")
        sys.stdout.write("\n")

if __name__ == "__main__":
    matrix = [[1,2,3],[4,0,6],[7,8,9]]
    print_matrix(matrix)
    set_zero(matrix)
    print "============"
    print_matrix(matrix)
