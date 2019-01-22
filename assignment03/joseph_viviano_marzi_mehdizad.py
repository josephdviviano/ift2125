#!/usr/bin/env python
# IFT 2125 : Devoir 3
# Etudiant 1 : Joseph Viviano
# Etudiant 2 : Marzi Mehdizadeh

import numpy as np

# DO NOT write anything outside functions and main (except imports)
# DO NOT call main()
# DO NOT change the methods names
# Please remove all the print functions used for debugging purposes
# Please change the filename according to your names
# Submit **only*** this file on Studium, NOT a .zip, NOT a full folder
# Remaining of the homework needs to be handed (in paper) before the demo.
#


def insert_sort(A):
    for idx in range(1, len(A)):

        this_val = A[idx]
        position = idx

        while position > 0 and A[position-1] > this_val:
            A[position] = A[position-1]
            position = position-1

        A[position] = this_val

    return(A)


def get_idx(seq, size):
        idx = []
        split = 1.0/size*len(seq)
        for i in range(size):
                idx.append(seq[int(round(i*split)):int(round((i+1)*split))])
        return(idx)


def merge(A, B):

    i, j = 0, 0
    l_sorted = []

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            l_sorted.append(A[i])
            i += 1
        else:
            l_sorted.append(B[j])
            j += 1

    while i < len(A):
        l_sorted.append(A[i])
        i += 1

    while j < len(B):
        l_sorted.append(B[j])
        j += 1

    #print('i={}/{} j={}/{}'.format(i, len(A), j, len(B)))
    return(l_sorted)


def mergesort4(A,n):

    if n <= 5:
        return insert_sort(A)

    else:

        idx = get_idx(list(range(len(A))), 4)

        l1 = A[idx[0][0]:idx[1][0]]
        l2 = A[idx[1][0]:idx[2][0]]
        l3 = A[idx[2][0]:idx[3][0]]
        l4 = A[idx[3][0]:idx[3][-1]+1]

        sl1 = mergesort4(l1, len(l1))
        sl2 = mergesort4(l2, len(l2))
        sl3 = mergesort4(l3, len(l3))
        sl4 = mergesort4(l4, len(l4))

        merged_12 = merge(sl1, sl2)
        merged_34 = merge(sl3, sl4)
        merged_list = merge(merged_12, merged_34)

    return(merged_list)


# Your code will be tested using tests similar to these ones.
# Be sure that it does not yield any error and that the two given tests give "True".
if __name__=="__main__":

    A = [2, 2, 1, 0, 4]
    print("Array : ", A)
    test1 = mergesort4(A, len(A)) == sorted(A)
    print("correctly sorted?", test1)

    B = np.random.randint(low = 0, high = 100, size = (20))
    print("Array : ", B)
    test2 = mergesort4(B, len(B)) == sorted(B)
    print("correctly sorted?", test2)

    print("Votre note serait =", np.mean([test1, test2])*100, "%" )


