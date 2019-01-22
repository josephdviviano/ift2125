#!/usr/bin/env python

import numpy as np

def roll_right(deg):
    # right to left
    for i in range(len(deg)-1, -1, -1):
        if deg[i] == 1:

            # edge of board, just remove
            if i == len(deg)-1:
                deg[i] = 0
            # shift threat to right
            else:
                deg[i+1] = 1
                deg[i] = 0

    return(deg)


def roll_left(deg):
    # left to right
    for i in range(len(deg)):
        if deg[i] == 1:

            # edge of board, just remove
            if i == 0:
                deg[i] = 0
            # shift threat to left
            else:
                deg[i-1] = 1
                deg[i] = 0

    return(deg)


def place_queen(promising, n, col, deg_45, deg_135):

    # we've filled the array, so we're good
    if promising[-1] != 0:
        return(promising)

    # tests each of the 8 possible positions on the board for this row
    for i in range(8):

        print('i={}, n={}'.format(i, n))
        print('current state:\npro={}\ndeg={}\ncol={}'.format(
            promising, deg_45+deg_135, col))

        if col[i] == 0 and deg_45[i] == 0 and deg_135[i] == 0:

            # add this item
            promising[n] = i+1

            # mark the out of bounds columns and diagonals for this row and
            # increment the out of bounds for the previous row
            deg_45 = roll_right(deg_45)
            def_135 = roll_left(deg_135)

            # add this row's blocks
            col[i] = 1
            if i-1 > 0:
                deg_135[i-1] = 1
            if i+1 < 8:
                deg_45[i+1] = 1

            # places the next queen
            promising = place_queen(promising, n+1, col, deg_45, deg_135)

            # we've filled the array, so we're good
            if promising[-1] != 0:
                return(promising)

            # failed to find the correct answer, so reset values
            col[i] = 0

            if i-1 > 0:
                deg_135[i-1] = 0
            if i+1 < 8:
                deg_45[i+1] = 0

            deg_45 = roll_left(deg_45)
            def_135 = roll_right(deg_135)

            promising[n] = 0

    # if we get here, we failed
    return(promising)


n_queens = 8

promising = np.zeros(n_queens)
col = np.zeros(n_queens)
deg_45 = np.zeros(n_queens)
deg_135 = np.zeros(n_queens)

promising = place_queen(promising, 0, col, deg_45, deg_135)
import IPython; IPython.embed()
