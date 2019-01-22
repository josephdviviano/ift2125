#!/usr/bin/env python

import numpy as np

def make_abacus(m, maxval=False):
    """ makes a 2xm-sized abacus """
    abacus = np.zeros((2, m)) # initalize array

    # 1 <= i <= m, A(1, i) < i and A(2, i) < i, therefore 0 when i = 1.
    for i in range(1, m):
        # add 1 to i because we convert 0 index to 1 index for problem

        if maxval:
            abacus[:, i] = i
        else:
            abacus[:, i] = np.random.randint(0, i+1, (1, 2))

    return(abacus)


def is_abacus(A):
    """ """
    # abacus must be 2xm
    dims = np.shape(A)
    if len(dims) > 2:
        return(False)

    n, m = dims
    if n != 2:
        return(False)

    # ensures all entries [:, i] in A are < i
    test =  make_abacus(m, maxval=True)
    if np.sum(A > test):
        return(False)

    # finally ensure [:, 0] is 0
    #if np.sum(A[:,0]):
    #    return(False)

    return(True)


def calc_weight(A):
    if not is_abacus(A):
        return(-1)

    else:
        m = A.shape[1]

        # initialize the w vector to hold all weights i=0:m (n.b): A has columns
        # ranging from 1:m, no 0th column.
        w = np.zeros((m+1))

        # add 1, for the base case w(0) = 1
        w[0] = 1

        for i in range(0, m):
            idx_1 = int(A[0, i])
            idx_2 = int(A[1, i])
            # shift iterator here to align length of w & A
            w[i+1] = w[idx_1] + w[idx_2]

        return(int(w[-1]))


def find_m(w):
    """given a weight, find the smallest abacus"""
    # first, note that the maximum weight of an abacus is (2*n!)+1
    # so we can first easily find the minimum size of the abacus by
    m, max_weight = 0, 0

    while max_weight < w:
        m += 1
        max_weight = calc_weight(make_abacus(m, maxval=True))

    print('w={}, m={}'.format(w, m))
    return(m)


def increment(i, j):
    """moves rightword through matrix, down columns"""
    j += 1 # move down in column
    if j == 2:
        j = 0  # goto top of next column
        i += 1 #

    return(i, j)


def deccrement(i, j):
    """moves leftword through matrix, up column"""
    j -= 1 # move up in column
    if j == -1:
        j = 1  # gotob bottom of previous column
        i -= 1 #

    return(i, j)


def fill_abacus(A, w, i=1, j=0):
    """Fills abacus such that it is legal and has the expected weight"""
    curr_weight = calc_weight(A) # intialize current_weight

    # the max value allowed in index=i (b/c python uses 0-based indexing)
    curr_val = i
    m = A.shape[1]

    # terminate illegal node i cannot be greater than the length of the matrix
    if i >= m:
        return(A)

    while curr_weight < w and curr_val >= 0:

        curr_weight = calc_weight(A)

        # SUCCESS: exactly correct, just return
        if curr_weight == w:
            print('success!')
            return(A)

        A[j, i] = curr_val
        print('A={}\nc={}/{}, i={}, j={}'.format(A, calc_weight(A), w, i, j))

        # FAILED: went over w, reset value at [j, i] and try again
        if calc_weight(A) > w:
            A[j, i] = 0
            print('failed :( :( :(')
            return(A)

        # go to child node
        else:
            next_i, next_j = increment(i, j)
            A = fill_abacus(A, w, i=next_i, j=next_j)
            curr_val -= 1

    #  if we have explored all options for m and not found a solution, try m+1
    if np.sum(A) == 0:
        A = fill_abacus(np.zeros((2, m+1)), w)

    # go to parent node
    return(A)

# 3a
#A = make_abacus(20)
#w = calc_weight(A)

# 3b
w = 20
m = find_m(w)
A = np.zeros((2, m))
A = fill_abacus(A, w)

