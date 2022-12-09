#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sqrd_list = []
    for i in matrix:
        sqrd_list.append(list(map(lambda x: x ** 2, i)))
    return sqrd_list
