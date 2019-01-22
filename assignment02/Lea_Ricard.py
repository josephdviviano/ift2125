#!/usr/bin/env python
# Write your names here :
# Student 1 :
# Student 2 :

import numpy as np
import random
import copy

# DO NOT write anything oustide functions and main (except imports)
# DO NOT call main()
# DO NOT change the methods names
# Please remove all the print functions used for debugging purposes
# Please maintain an average of +-80 characters by line >..........>.............>..............>..............>..............>................>......not like this
# Please change the filename according to your names
# Submit **only*** this file on Studium, NOT a .zip, NOT a full folder
# Remaining of the homework needs to be handed (in paper) before the demo.

def random_graph(n,m):
    # Input : size n, m
    # Output : matrice representant A[i][j] = 1 ssi S_i contient l'element j

    # A completer...
    # Look at Demo5 for inspiration on how to use random package
    A = np.random.randint(2, size=(m, n)) # need to create the nxm boolean array here

    return A

def intersection(matrice):
    n, m = matrice.shape
    S = []
    L = [i for i in range(n)]  # List of all Si
    C = [j for j in range(m)]  # List of all columns

    for i in range(n):
        sumline = 0
        for j in range(m):
            sumline += matrice[i][j]
        if sumline == 0:
            return set()

    while len(L) !=0:
        idxsumcolumnmax = 0
        sumcolumnmax = 0
        for i in C:
            sumcolumn = 0
            for j in L:
                sumcolumn += matrice[j][i]
            if sumcolumn >= sumcolumnmax:
                sumcolumnmax = sumcolumn
                idxsumcolumnmax = i
        S.append(idxsumcolumnmax+1)

        #Remove candidates from L and C
        Lcopy = copy.copy(L)
        for k in range(len(Lcopy)):
            if matrice[Lcopy[k]][idxsumcolumnmax] == 1:
                L.remove(Lcopy[k])
        C.remove(idxsumcolumnmax)
    return set(S)


def experiment(n, m, nb_experiments):
    # Cette fonction doit rester exactement comme ceci
    # Do not change anything here
    size_of_S = []
    for exp in range(nb_experiments):
        A = random_graph(n, m)
        S = intersection(A)
        print(S)
        size_of_S.append(len(S))
    return size_of_S



if __name__=="__main__": # main() will only be called when using "python file.py"
    # Rien d'autre ne doit etre necessaire dans le main pour retourner moyenne/std
    # Nothing else should go there when you submit your code, do not change anything
    n = 20
    m = 100
    k = 50

    size_of_S = experiment(n, m, k)
    # Ceci devrait vous donner la moyenne et ecart-type
    print("mean", np.mean(size_of_S), "std", np.std(size_of_S))


