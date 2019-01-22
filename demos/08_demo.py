
# coding: utf-8

# # Demo 8 - 23 mars 2018
# ## Stéphanie Larocque
#

# In[1]:


import numpy as np


# ## Question 1 : Donner un algorithme (programmation dynamique) pour rendre la
# monnaie avec le moins de pièces possibles, en supposant que chaque type de
# pièce existe en quantité illimitée.

def nb_pieces(coins, M):
    # coins = [c1, c2, ..., cn] les differentes denominations
    # M = le montant total a obtenir

    # Retourne le tableau T tel que:
    # T[i,j] = nombre minimal de pieces des denominations c[1]...c[i] pour obtenir un montant j
    # T[i,j] = +inf si impossible

    n = len(coins)               # nombre de denominations differentes
    T = np.zeros( (n, M+1) )     # tableau de zeros

    for i in range(n):
        for j in range(1,M+1):
            a = T[i-1, j] if i>0 else float("inf")          # on ne prend pas c[i]
            b = T[i, j-coins[i]] if j>=coins[i] else float("inf")  # on prend c[i]
            T[i,j] = min(a, b+1)
    return T

coins = [2, 4, 6]
M = 7
nb_pieces(coins, M)


def monnaie(coins, M):
    # coins = [c1, c2, ..., cn] les differentes denominations
    # M = le montant total a obtenir

    # Retourne le nombre de pieces de chaque denomination afin d'obtenir le
    # montant M

    T = nb_pieces(coins, M)
    n = len(coins)
    if T[n-1,M]==float("inf"):
        return "Solution impossible"      # par exemple, si c=[2,4] et M = 3


    pieces = [] # indiquera les pieces a prendre
    i = n-1
    j = M

    # On part de la derniere case T[n-1, M] et on retrouve le chemin
    # jusqu'a T[0,0]
    while (i,j)!=(0,0):

        a = T[i-1, j] if i>0 else float("inf")
        b = T[i, j - coins[i]] if j>=coins[i] else float("inf")

        if T[i,j]==a:
            i = i-1
        elif T[i,j]==b+1 :
            j = j - coins[i]
            pieces.append(coins[i])

    print("Les dénominations sont :", coins)
    print("Il faudra prendre les pieces de", pieces,
          "(pour un total de", int(T[n-1, M]), "pieces) afin d'obtenir", M, '$')
    return pieces

c = [1,3,5,6]
M = 7

monnaie(c, M)


# ## Question 2 : Donner un algorithme qui rend la monnaie même lorsque le
# nombre de pièces disponibles est limité.

def nb_pieces_limite(coins, limite, M):
    # c = [c1, c2, ..., cn] les differentes denominations
    # l = [l1, l2, ..., ln] le nombre de pieces maximum de chaque denomination
    # M = le montant total a obtenir

    # Retourne le tableau T tel que:
    # T[i,j] = (x, y) ou x = nombre minimal de pieces des denominations
    # c[1]...c[i] pour obtenir un montant j
    #                    y = [p1, p2, ..., pn] le nombre de pieces de chaque
    #                        denomination utilisees a date
    # T[i,j] = +inf si impossible


    # liste des pieces disponibles
    # p = [0, c1, c1, .., c1, c2, .., c2, ....., cn, ..., cn]
    p = [0] + [coins[i] for i in range(len(coins)) for j in range(limite[i])]
    nb_total_pieces_disponibles = len(p)
    print("Pièces disponibles", p)

    T = np.full( (len(p)+1, M+1), float("inf") ) #tableau de +infini
    for i in range(len(p)):
        T[i][0] = 0  # 0 piece pour un montant de 0$

    for i in range(1,len(p)):
        for j in range(1,M+1):
            # p[i] d.n.e == a
            a = T[i-1, j]      if  i>0              else float("inf")
            b = T[i-1, j-p[i]] if (i>0 and j>=p[i]) else float("inf")
            T[i,j] = min(a, b+1)
    return T


def monnaie_limite(coins, limite, M):
    # c = [c1, c2, ..., cn] les differentes denominations
    # M = le montant total a obtenir
    # l = [l1, l2, ..., ln] le nombre de pieces maximum de chaque denomination
    # Retourne les pieces de chaque denomination necessaires afin d'obtenir le montant M
    T = nb_pieces_limite(coins, limite, M)
    # enumeration de toutes les pieces disponibles, avec repetition
    p = [0] + [coins[i] for i in range(len(coins)) for j in range(limite[i])]
    pieces = [] # indiquera les pieces necessaires (le resultat)
    j = M

    if T[len(p)-1,M]==float("inf"):
        return "Solution impossible" # par exemple, si c=[2,4] et M = 3

    # On part de la derniere case T[len(p)-1, M] et on retrouve le chemin jusqu'a T[0,0]
    for i in range(len(p)-1, 0, -1):
        a = T[i-1, j]
        b = T[i-1, j - p[i]] if j>=p[i] else float("inf")

        if T[i,j]==b+1 :
            j = j - p[i]
            pieces.append(p[i])

    print("Les dénominations sont :", coins, "limite", limite)
    print("Il faudra prendre les pieces de", pieces,
          "(pour un total de", int(T[len(p)-1, M]), "pieces) afin obtenir", M, '$')
    return pieces

coins  = [1,3,10,20]
limite = [1,1,1,1]
M = 43

print("limité", monnaie_limite(coins, limite, M))
print("")
print("illimité", monnaie(coins, M))


def expomod(a, n, z):
    i = n
    r = 1
    x = a%z
    while i>0:
        if i%2==1:
            r = (r*x)%z
        x = (x*x)%z
        i = i//2
    return r

# Demo 7
def pgcd_etendu(a, b):
    if b==0:
        return (1,0,a)
    else:
        s1, t1, d = pgcd_etendu(b, a%b)
        return (t1, s1-(a//b)*t1, d)

def inverse(a, b):
    #return inverse of a mod b when pgcd(a, b)==1
    s, t, d = pgcd_etendu(a,b)
    if d == 1:
        return s
    else:
        print("pgcd(a, b)!=1")

# Bob
p = 19
q = 23
z = p*q #437
phi = (p-1)*(q-1)
n = 13

s = inverse(n, phi)

print("p =", p, ", q =", q,  ", z =", z, ", n =", n, ", phi =", phi, ", s =", s)


# Bob affiche publiquement :
# - z = 437
# - n = 13
#
# mais garde secrètement :
# - s = 61

# In[14]:


# Alice
m = 123 #message a envoyer
c = expomod(m, n, z)
print("Message m =", m, "encrypté m^n(mod z):", c)

# Bob lorsqu'il recoit le message
print("Message décodé c^s(mod z):", expomod(c, s, z))

