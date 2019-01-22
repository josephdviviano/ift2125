#!/usr/bin/env python

import numpy as np
import random # import packages to generates random numbers

def random_graph(n):
    # Input : nombre de sommets du graphe, n
    # Output : matrice d'adjacence A de taille nxn où A[i][j] = A[j][i] = 1 ssi les sommets i et j sont reliés
    # Ici on considère donc un graphe simple non orienté dont tous les poids sont 0

    # Generates a nXn matrix A containing only 0s and 1s
    A = np.array([[random.randint(0,1) for i in range(n)] for j in range(n)])

    # Make A great again (i.e. make A an adjacency matrix for simple undirected graph)
    for i in range(n):
        A[i,i] = 0 # No loops on a single vertex

    for i in range(n):
        for j in range(n):
            A[j,i]=A[i,j] # Since undirected graph, A[i][j] = A[j][i]

    return(A)


def compare(A, B):
    # Input : 2 graphs A and B
    # Output : True if they may be isomophic (i.e. si même nombre de sommets, d'arêtes et de séquence de degrés),
    #          False otherwise

    # Check if they have same number of vertex
    if len(A)!=len(B):
        print("Not the same number of vertices")
        return False

    if np.sum(A)!=np.sum(B): #np.sum(A) = (number of edges in A) * 2, each edge counted 2 times
        print("Not the same number of edges")
        return False

    deg_A = [np.sum(A_i) for A_i in A]
    deg_B = [np.sum(B_i) for B_i in B]
    if sorted(deg_A) != sorted(deg_B):
        print("Not the same degrees sequence")
        return(False)

    # Are not necessarily 2 isomorphic graphs, but... maybe.
    return(True)


A = random_graph(3)
B = random_graph(3)
print("Adjacency matrix A\n", A)
print("Adjacency matrix B\n", B)
print("Peuvent être isomorphes ?",compare(A,B))


def find(D,x):
    S, H = D
    parent = S[x]
    while parent!=x:
        x = parent
        parent = S[x]
    return parent


def merge(D, a, b):
    # Merge the disjoint sets labelled a and b

    S, H = D
    if a==b:
        return (S, H)

    height_a = H[a]
    height_b = H[b]

    if height_a == height_b: # on prend la root_b comme racine, la taille augmente de 1
        S[b] = a
        H[a] += 1

    elif height_a > height_b:
        S[b] = a

    elif height_a < height_b:
        S[a] = b

    return (S, H)

# Disjoint sets {0},{1,3,7},{2,5,6,10},{4,9},{8}
# D = (S,H) où S[i] = parent de i, et H[root] = hauteur de l'arbre avec racine "root"
D=([0, 1, 2, 1, 4, 2, 2, 1, 8, 4, 5],
   [0, 1, 2, 0, 1, 0, 0, 0, 0, 0, 0])
print("D:",D)
print("Find 8:", find(D, 8))
print("Find 10:", find(D,10))

D2 = merge(D, 8, 10)
print("D2:",D2)
print("Find 8:", find(D2, 8))
print("Find 10:", find(D2, 10))


# ## Question 4
#
# ### Implémenter l'algorithme de Kruskal et analyser son temps d'exécution dans le pire cas.
#
# Solution: Voici une implémentation python basée sur l'implémentation d'ensembles disjoints de l'exercice précédent, pour déterminer si une arête doit être rajoutée ou pas à l'arbre courant $T$

# In[9]:


def kruskal(n,E):
    # Input : n (nombre de sommets) et E (une liste de [[arete e =(u,v), poids],[...],])
    # Output : Arbre sous-tendant de poids minimal

    E = sorted(E, key=lambda elem:elem[1]) #sort the edges in increasing weight  #O(m log m)

    T = [] # Va contenir l'arbre sous-tendant de poids minimal
    w = 0  # Total weight of minimal tree
    D = ([i for i in range(n)], [0 for i in range(n)] ) # O(n)

    while len(T)!= n-1: # enter this loop at most O(m) times
        (u,v), weight = E.pop(0) # pop first element of E (minimal edge) # O(1)
        comp_connexe_u = find(D, u) # O(log n)
        comp_connexe_v = find(D, v) # O(log n)

        if comp_connexe_u != comp_connexe_v: #si pas dans la même composante # enter this loop O(n) times
            T.append((u,v)) # rajouter l'arête à l'arbre minimal # O(1)
            w += weight # ajuster le poids total
            D = merge(D, find(D,u), find(D,v)) # fusionner les 2 composantes connexes ensemble # O(1)
    return (T, w)


# In[10]:


G = np.array([
[0,1,0,4,0,0,0],
[1,0,2,6,4,0,0],
[0,2,0,0,5,6,0],
[4,6,0,0,3,0,4],
[0,4,5,3,0,8,7],
[0,0,6,0,8,0,3],
[0,0,0,4,7,3,0]])

n = 7
E = [[(0, 1), 1], [(1, 2), 2], [(3, 4), 3], [(5, 6), 3],
     [(0, 3), 4], [(1, 4), 4], [(3, 6), 4], [(2, 4), 5],
     [(1, 3), 6], [(2, 5), 6], [(4, 6), 7], [(4, 5), 8]]

T, w = kruskal(n, E)
print("Arbre sous-tendant minimal (de poids "+str(w)+") :", T )


# ## Question 5
#
# ### Implémenter une variante de l'algorithme de Kruskal tel que, pour un k donné, l'algorithme retourne une partition des n sommets du graphe en k ensembles (disjoints) de manière à maximiser la distance entre toute paire de points provenant d'ensemble différents.

# In[11]:


def clustering(n, E, k):
    # Input :
    # n : number of vertices
    # E : set of edges {[(1,2), weight 1],[(3,4) , weight_2]} means 1--2 (weight 1) and 3--4 (weight2)
    # k : number of clusters
    #
    E = sorted(E, key=lambda elem:elem[1]) #sort the edges in increasing weight
    T = [] # va contenir l'arbre sous-tendant de poids minimal
    w = 0 #Total weight of minimal tree
    D = ([i for i in range(n)], [1 for i in range(n)] )

    while len(T)!= n-k: # the only difference is here, k = 1 for kruskal
        (u,v), weight = E.pop(0) # pop first element of E (minimal edge)
        comp_connexe_u = find(D, u)
        comp_connexe_v = find(D, v)

        if comp_connexe_u != comp_connexe_v: #si pas dans la même composante
            T.append((u,v)) # rajouter l'arête à l'arbre minimal
            w += weight # ajuster le poids total
            D = merge(D, u, v) # fusionner les 2 composantes connexes ensemble
    return (T, w)



# In[12]:


clustering(n, E, 4)

