#!/usr/bin/env python
# Student 1 : Joseph D Viviano
# Student 2 : Marzi Mehdizad
"""
a) yes.
   m = {1,2,3,4,5,6}
   s_1 = {1,2}
   s_2 = {3,4}
   s_3 = {1,2,3,4}
   S = {{}, {5}, {6}, {5,6}}

   + contains empty
   + heridity, yes, {5} and {6} inherited from {5,6}
   + exchangability, yes, {6} and {5} can be exchanged to produce {5,6}, no
     new sets are created.

b) no. if this procedure never returns an empty set, it cannot be a matroid! a
   matroid always contains an empty set (trivial condition!)
   m = {1,2,3,4,5,6}
   s_1 = {1,2}
   s_2 = {3,4}
   s_3 = {1,2,3,4}
   S = {{1}, {2}, {3}, {4}, {1,2}, {1,3}, ..., {1,2,3,4}}

"""

import numpy as np
import random
import sys


def random_graph(n,m):
    """
    Input : size n, m
    Output : matrix -- A[i,j] = 1 if S_i contains the element j (boolean)
    """
    return(np.random.randint(2, size=(n, m)))


def intersection(A):
    """
    Calculates the set S of minimum cardinality with the set of sets {S1...Si}.

    First, we ensure there are no empty sets in A, otherwise we return an empty
    set (since there is no solution).

    Next we initialize an empty array of zeros to represent S (min_card).

    Then, we take the sum of A along it's columns to get the counts of each
    element's participation across the m sets. Our selection function is that
    which selects the set element that contributes to the most sets in A.

    We add this selected element to min_card, and remove all rows of A that are
    accounted for by this set element.

    We repeat this until the array A is empty.
    """
    # feasibility fxn: if any set in A is empty, return an empty set since our
    # task is impossible
    if len(np.where(np.sum(A, axis=1) == 0)[0]) > 0:
        return(set())

    # stores the S of minimum cardinality (as the characteristic fxn)
    min_card = np.zeros(A.shape[1]).astype(np.int)

    # 1, 2, ..., n
    all_n = np.arange(1, len(min_card)+1)

    # solution fxn: A will be empty is min_card accounts for all sets in A
    while np.shape(A)[0] != 0:

        # counts the number of S_i that each element of the set contributes to
        S_count = np.sum(A, axis=0)

        # selection fxn: finds the current new set element that contributes to
        # the maximum number of S_i's (implicitly tiebreaks using [-1])
        this_max = all_n[S_count == np.max(S_count)][-1]
        min_card[this_max-1] = 1

        # remove the rows of A that we account for during this iteration
        idx_remove = np.where(A[:, this_max-1])[0]
        A = np.delete(A, idx_remove, 0)

    # objective fxn: returns the set of elements in min_card
    S = set(all_n[min_card.astype(np.bool)])

    return(S)


def experiment(n, m, nb_experiments):
    """Calculates the size of the minimum cardinal sets across nb_experiments"""
    size_of_S = []

    for exp in range(nb_experiments):
        A = random_graph(n, m)
        S = intersection(A)
        size_of_S.append(len(S))

    return(size_of_S)


if __name__=="__main__":

    n = 20
    m = 100
    k = 50

    size_of_S = experiment(n, m, k)
    print("mean", np.mean(size_of_S), "std", np.std(size_of_S))


