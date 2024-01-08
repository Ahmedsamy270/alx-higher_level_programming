#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            for x in range(len(matrix[i])):
                if matrix[i][x] != matrix[i][-1]:
                    print("{:d}".format(matrix[i][x]), end=" ")
                else:
                    print("{:d}".format(matrix[i][x]), end="")
            print()
    else:
        return
