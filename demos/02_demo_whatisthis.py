#!/usr/bin/env python
"""Multiplying permutations."""

from demo02_examples import *

l = []
for i in range(10):
    l.append(i)

# list comprehension to generate list of tuples
l = [(i,j) for i in range(10) for j in range(2)]

# permutations as tuples
p = (2, 1, 4, 5, 3) # 1 -> 2, 2 -> 1, 3 -> 4, 4 -> 5, 5 -> 3

def product(q,p):
    return(tuple( [ q[p[i]-1] for i in range(len(p)) ] ))

def inverse(p):
    return(tuple( [p.index(i)+1 for i in range(1, len(p)+1) ] ))

def sift(p, T):
    m = len(p)
    IDENTITY = tuple(range(1, m+1))

    while p != IDENTITY:
        i = min(x for x in range(m) if p[x] != x+1)
        j =

