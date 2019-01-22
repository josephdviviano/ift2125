#!/usr/bin/env python

import numpy as np
import sys

def fibbonacci(n):
    memory = np.zeros(n+1)
    memory[0] = 0
    memory[1] = 1

    for i in range(2, n+1):
        value = memory[i-1] + memory[i-2]
        memory[i] = value

    print('fibbonaci series: {}'.format(memory))
    return(memory[-1])

try:
    n = sys.argv[1]
except:
    n = 10

answer = fibbonacci(n)
print('{}th fibbonacci number is {}'.format(n, answer))
