#!/usr/bin/env python

import numpy as np

def optimize(weight, value, capacity, multiplier):

    # compute new multiplied weights, values
    new_weights = []
    new_values = []

    for i, mult in enumerate(multiplier):
        new_weights.extend([weight[i]]*mult)
        new_values.extend([value[i]]*mult)

    weight = new_weights
    value = new_values

    # initialize values
    n_objects = len(weight)

    T = np.zeros((n_objects+1, capacity+1)) # +1 so we have base case capacity=0

    for j in range(1, capacity+1, 1):
        T[0, j] = 0

    # i : object under consideration
    # j : curent target weight

    for i in range(1, n_objects+1, 1):
        for j in range(1, capacity+1, 1):

            replace_weight = j - weight[i-1]
            replace_value = value[i-1]

            # impossible to replace, so we just carry the state forward
            if replace_weight < 0:
                T[i, j] = T[i-1, j]

            # max of carrying state forward, and using the state found in
            # j - weight[i-1], the 'replacement weight' PLUS the new value
            # note that the replacement weight should be target weight - the
            # weight of the object we're currently adding (which is why we have
            # to look at the configuration at that state, j-weight[i-1), to know
            # how much weight we would have had then
            else:
                T[i, j] = max(T[i-1, j], T[i-1, replace_weight] + replace_value)

    max_value = T[-1, -1]
    i = n_objects
    j = capacity
    objects = []

    # work backwards through the table to find the objects that contributed
    while i > 0:

        # if these two values are equal, object i did not contribute
        if T[i, j] == T[i-1, j]:
            i -= 1

        # if T[i, j] == T[i, j - weight[i-1]] + value[i-1] we must have added
        # one of object i!
        elif T[i, j] != T[i-1, j] and T[i, j] == T[i, j - weight[i-1]] + value[i-1]:
            objects.append((weight[i-1], value[i-1]))
            j -= weight[i-1]

    return(T, objects, max_value)

weight = [1, 2, 5, 6, 7]
value  = [1, 6, 18, 22, 28]
multiplier = [2, 2, 2, 2, 2]
capacity = 22

T, objects, max_value = optimize(weight, value, capacity, multiplier)

#pt.print(T)

print('knapsack weight={}, objects:\n+ weight = {}\n+ value = {}\n'.format(
    capacity, value, max_value))
print('{}\nobjects={}, total_value={}'.format(T, objects, max_value))

