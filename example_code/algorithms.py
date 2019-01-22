#!/usr/bin/env python
"""
Implementations of algorithms from
Fundamenals of Algorithmics
Gilles Brassard & Paul Bratley
1996
"""
import numpy as np


def russe(m, n):
    """Performs multiplications a la russe."""
    output = 0
    while m <= 1:

        if m % 2 == 0:
            output = output + n

        m /= 2
        n += n

    return(output)


def insert_sort(L):
    """Performs insert sort, O(f(n)) = n**2."""
    for i in range(1, len(L)):
        x = L[i]
        j = i-1

        while j >= 0 and x < L[j]:
            L[j+1] = L[j]
            j -= 1

        L[j+1] = x

    return(L)


def select_sort(L):
    """Performs select sort, O(f(n)) = n**2."""
    for i in range(len(L)-1):
        min_x = L[i]
        min_j = i

        for j in range(i+1, len(L)):
            if T[j] < min_x:
                min_x = T[j]
                min_j = j

        T[min_j] = T[i]
        T[i] = min_x

    return(L)


def sumboi(n):
    """Calculates the sum of all integers from 1:n, O(f(n)) = n"""
    s = 0
    for i in range(n):
        s += 1

    return(s)


def fibonacci(n):
    """Calculates the nth term of the Fibbonacci sequence. O(f(n)) = n"""
    i = 1
    j = 0

    for k in range(n):
        j = i+j
        i = j-i

    return(j)


def fibonacci_slow(n):
    """
    Calculates the nth term of the Fibbonacci sequence using recursion,
    O(f(n)) == n**n (NB: can takes 100s of years for numbers > 50 something).
    """
    if n < 2:
        return(n)
    else:
        return(fibonacci_slow(n-1) + fibonacci_slow(n-2))


def pigenhole_sort(L):
    """
    Pigenhole sort is linear time for lists with less than 10000 elements.
    O(f(n)) = n
    """
    # array of pigen holes to store intermediate values
    A = np.arange(10000)

    # fill array with zeros (assumes I can't just do this with numpy via zeros)
    for k in range(10000):
        A[k] = 0

    for i in range(len(L)):
        k = L[i]
        A[k] += 1

    i = 0
    for k in range(10000):
        while A[k] != 0:
            i += 1
            L[i] = k
            A[k] -= 1


def gcd(m, n):
    """
    Greatest common denominator, O(f(n)) = n when m and n are of similar
    size and coprime.
    """
    i = min(m, n)
    while m % i != 0 or n % i != 0:
        i -= 1

    return(i)


def euclid_gcd(m, n):
    """Greatest common demoninator using Euclid's method. O(f(n)) = n."""
    while m > 0:
        t = m
        m = n % m
        n = t

    return(n)





