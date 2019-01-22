#!/usr/bin/env python

import numpy as np

def get_ways(req_change, coinlist):
    """ """
    n_change = req_change + 1  # add a base case of required change = 0
    n_coins = len(coinlist) + 1

    T = np.zeros((n_coins, n_change))

    # initialize boundary values to inf, so they never win the min (below)
    for j in range(1, n_change, 1):
        T[0, j] = np.inf

    # i is the amount of money we need to make change for
    for i in range(1, n_coins, 1):
        for j in range(1, n_change, 1):

            # last_val is the value remaining if we are to add a single coin
            # of the current denomination, which removes n coins of the previous
            # denomination
            last_val = j-coinlist[i-1]

            # last_val cannot be less than zero, because python indexing wraps
            if last_val < 0:
                T[i, j] = T[i-1, j]
            else:
                T[i, j] = min(T[i-1, j], 1 + T[i, last_val])


    # find coins used
    i = n_coins-1
    j = n_change-1
    coins_used = []

    while j > 0:
        print('i={},j={}'.format(i,j))
        print(T)

        if T[i, j] == T[i-1, j]:
            i -= 1
        elif T[i, j] != T[i-1, j]:
            coins_used.append(coinlist[i-1])
            j -= coinlist[i-1]

    return(T, coins_used, T[-1, -1])

req_change = 8
coinlist = [1, 4, 6]
T, coins, answer = get_ways(req_change, coinlist)

print('problem: change for {}, using coins={}'.format(req_change, coinlist))
print('solution:\n{}\n\nusing {} coins: {}'.format(T, answer, coins))

