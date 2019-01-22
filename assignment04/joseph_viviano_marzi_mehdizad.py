#!/usr/bin/env python

# IFT 2125 : Devoir 4
# Etudiant 1 : Joseph Viviano
# Etudiant 2 : Marzi Mehdizad

import numpy as np

# DO NOT write anything outside functions and main (except imports)
# DO NOT call main()
# DO NOT change the methods names
# Please remove all the print functions used for debugging purposes
# Please change the filename according to your names
# Submit **only*** this file on Studium, NOT a .zip, NOT a full folder
# Remaining of the homework needs to be handed (in paper) before the demo.


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
    """
    Checks the following 4 conditions:
    1) The abacus can be a numpy array (i.e., is rectangular)
    2) The abacus is 2D
    3) The abacus is 2xm
    4) The abacus entries are all valid
    """

    # if A is two lists [[A], [B]] of different lengths, this will fail
    try:
        A = np.array(A)
    except:
        return(False)

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


def abacus_weight(A):
    """ calculates weight of abacus, returns -1 if A is not an abacus """

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
        max_weight = abacus_weight(make_abacus(m, maxval=True))

    #print('w={}, m={}'.format(w, m))
    return(m)


def increment(i, j):
    """ moves rightword through matrix, down columns """
    j += 1 # move down in column
    if j == 2:
        j = 0  # goto top of next column
        i += 1 #

    return(i, j)


def deccrement(i, j):
    """ moves leftword through matrix, up column """
    j -= 1 # move up in column
    if j == -1:
        j = 1  # goto bottom of previous column
        i -= 1 #

    return(i, j)


def fill_abacus(A, w, i=1, j=0):
    """
    fills abacus such that it is legal and has the expected weight at the
    smallest possible size.

    this is a backtracking procedure that begins with an all-zero abacus of
    length m. m can be initialized to a reasonable value to avoid unnessicary
    work, i.e., only searching an abacus that could potentially contain the
    target weight w by searching the maximum weights of each abacus size.

    the algorithm proceeds as follows: at the parent node of the recursion tree,
    we loop through all valid values of the abacus at location [j, i], starting
    from the largest legal value. if we add this value and the current weight
    of the abacus is still less than the target, we resursively call the
    algorithm to loop through all legal values in [increment(i,j)].

    increment moves rightword through the abacus, down columns.

    if we go over the target weight of the abacus, the current child node sets
    it's [j, i] to 0 (undoing it's own work), and returns the unaltered abacus,
    so the for loop in the parent node can try the next smallest legal value for
    location [j, i].

    in this way, the algorithm is a depth-first search of the possible legal
    abacus configurations. After building the first branch of the recursion
    tree, the algorithm searches abacuses of successively smaller weights.

    if at any point an abacus is produced with the correct weight, it is
    returned through all parent nodes, and the algorithm is done.

    if this procedure finishes completely, and the abacus returned is all zeros,
    no solution was found. therefore the root of the tree conducts a new
    recursive call with a new all-zero abacus of size m+1. In this way, the
    algorithm searches m successively until it finds the first soltion, which
    is garunteed to be the smallest possible m (that is >= the m of the original
    abacus).
    """
    curr_weight = abacus_weight(A) # intialize current_weight

    # the max value allowed in index=i (b/c python uses 0-based indexing)
    curr_val = i
    m = A.shape[1]

    # terminate illegal node: i cannot be greater than the length of the matrix
    if i >= m:
        return(A)

    # at this node, try all valid values at [j, i], descending
    while curr_weight <= w and curr_val >= 0:

        curr_weight = abacus_weight(A)

        # SUCCESS: exactly correct, just return all the way up the tree
        if curr_weight == w:
            return(A)

        A[j, i] = curr_val
        print('Abacus:\n{}\nc={}/{}, i={}, j={}'.format(
            A, abacus_weight(A), w, i, j))

        # FAILED: went over w, reset value at [j, i] and try again
        if abacus_weight(A) > w:
            A[j, i] = 0
            return(A)

        # go to child node
        else:
            next_i, next_j = increment(i, j)
            A = fill_abacus(A, w, i=next_i, j=next_j)
            curr_val -= 1

    #  if we have explored all options for abacus length m and not found a
    #  solution, try m+1
    if np.sum(A) == 0:
        A = fill_abacus(np.zeros((2, m+1)), w)

    # go to parent node
    return(A)


def minimal_size_abacus(w):
    """
    First, calculates the minimum sized abacus that can contain
    weight w, which we call m. Then, constructs a 2xm all-zero
    abacus, which is submitted to the backtracking fill_abacus
    function. This function expects a numpy array. The result is
    finally returned as a list.
    """

    # Input : integer w>=1
    # Output : abaque of minimal size
    m = find_m(w)
    A = np.zeros((2, m))
    A = fill_abacus(A, w)
    # converts numpy array to list to maintain compatibility with tests
    return(A.tolist())


# Your code will be tested using tests similar to these ones.
# Be sure that it does not yield any error and that the two given tests give "True".
if __name__=="__main__":
    A1 = np.array([[0, 1, 2, 3, 4], [0, 1, 0, 2, 2]])
    A2 = np.array([[0, 0, 0, 0, 3], [0, 1, 2, 3, 4]])
    A3 = np.array([[0, 2, 2, 2], [0, 1, 2, 3]])
    A4 = np.array([[10], [0]])

    # Answers should be
    # 13, 9, -1, -1

    print("3a:")
    print("A1", int(abacus_weight(A1)) == 13)
    print("A2", int(abacus_weight(A2)) ==  9)
    print("A3", int(abacus_weight(A3)) == -1)
    print("A4", int(abacus_weight(A4)) == -1)

    print("3b:")
    w1 = 4
    result1 = list([[0,1],[0,1]])
    A = minimal_size_abacus(w1)
    print(list(minimal_size_abacus(w1)) == result1)

    minimal_size_abacus(6)

