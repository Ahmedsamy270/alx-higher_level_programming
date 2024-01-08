#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            for x in range(len(matrix[i])):
                print("{:d}".format(matrix[i][x]), end=" " if matrix[i][x] != matrix[i][-1] else "")
            print()
    else:
        return
