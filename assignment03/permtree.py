#!/usr/bin/env python

import numpy as np
from math import factorial

def shift(array):
    """Requires n switches, each operating on one output"""
    #return(np.append(array[1:], array[0]))
    return(np.append(array[-1], array[:-1]))


def permtree(i, j, n, array):
    """
    first, generates an array of n numbers, then yields+shifts n times, at
    each level of the recursion tree. Requires n*log(n) 'switch' operations
    (n switches for shift(), log(n) for each level of tree).
    """

    # start at the nth level of the tree
    if i < n:
        permtree(i+1, 1, n, np.append(array, i+1))

    # prints and shifts one child
    print(tuple(array))
    array = shift(array)

    # returns n children of nth level of the tree on each branch
    if j < i:
        permtree(i, j+1, n, array)
    else:
        # returns to n-1 level of the tree
        return


n = 4
permtree(1, 1, n, np.array([1]))

print('n switches (n logn) = {}'.format(np.log2(n) * n))
