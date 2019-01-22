#!/usr/bin/env python
"""Section 8.2 of Brassard + Bratley."""

import numpy as np

def make_change(denominations, change):

    # table: row per denomination, column per amount of change
    #        both +1 so we can have a base case of c[0,0] = 0
    c = np.zeros((len(denominations)+1, change+1))
    c[0,:] = np.inf # denotes an impossible solution

    # start search from c[1,1]
    for i in range(1, len(denominations)+1):
        for j in range(1, change+1):

            use_prev = c[i-1, j] # when i=1, i-1 = inf, which will always lose
            use_this = 1+c[i, j-denominations[i-1]]

            # the smallest denomination > required amount of change
            if i == 1 and j < denominations[i-1]:
                c[i, j] = np.inf

            # use denomination[i-1], because we dont have any other option
            elif i == 1:
                c[i, j] = use_this

            # change required < than denomination[i-1], use last answer
            elif j < denominations[i-1]:
                c[i, j] = use_prev

            # use the smaller of this answer and the last answer
            else:
                c[i, j] = min(use_prev, use_this)

            print('[{},{}]: prev={}, this={}'.format(i, j, use_prev, use_this))

    return(c, int(c[len(denominations), change]))


def retrieve_coins(c, denominations):
    dims = np.shape(c)
    i = dims[0]-1
    j = dims[1]-1
    coins_used = []

    while i > 0 and j > 0:

        # the same answer can be found with the i-1 denomination
        if c[i, j] == c[i-1, j]:
            i -= 1

        # use one of these coins, and move j to j-denominations[i-1]
        elif c[i, j] == 1+c[i, j-denominations[i-1]]:
            coins_used.append(denominations[i-1])
            j -= denominations[i-1]

    return(coins_used)


change = 8
denominations = [1,4,6]
table, n_coins = make_change(denominations, change)
coins_used = retrieve_coins(table, denominations)

print('{} coins required to make change for {} dollars using coins={}'.format(
    n_coins, change, denominations))
print('used coins: {}'.format(coins_used))
print('full table:\n{}'.format(table))

