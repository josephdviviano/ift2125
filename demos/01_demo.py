#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# Q1: find the smallest common divider of two large numbers
def smallest_common_divider(a, b):
    while b != 0:
        a, b = b, a%b # remainder of a/b
    return(a)


def smallest_common_multiple(a, b):
    return(a*b / smallest_common_divider(a, b))


# Q2: sort a list using insertion sort
def insertion_sort(l):
    """sort items from low-->high"""
    n = len(l)

    # iter through list
    # nb: range(10, 0 , -2) -- count backwards from 10 to 0 in 2s
    for i in range(n-1):
        idx_min = i

        # compare lower item with known minimum
        for j in range(i+1, n):
            if l[j] < l[idx_min]:
                idx_min = j

        l[i], l[idx_min] = l[idx_min], l[i]
        print('step {}:{}'.format(i, l))
    return(l)


# Q3: calculate the determinant of a matrix
def sub_matrix(A, i, j):
    """removes row i and column j"""
    A = np.delete(A, (i), axis=0) # delete row i
    A = np.delete(A, (j), axis=1) # delete col j

    return(A)


def det(A):
    i = 0
    m = len(A) # number of rows

    # recursion stops
    if m == 1:
        return(A[0,0]) # single row
    else:
        x = 0
        for j in range(m):
            x += ( (-1)**(i+j) ) * A[i,j] * det(sub_matrix(A, i, j)))

    return(x)


A = np.array( [[1,2,30,1], [4,5,5,1], [7,8,9,1]] )
print("Determinant of\n{} is {}".format(A, det(A)))
print("Determinant with numpy: {}".format(np.linalg.det(A)))

print(len(A))    # number of lines
print(len(A[0])) # number of columns

