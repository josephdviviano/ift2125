#!/usr/bin/env python

import numpy as np

class Times:
    """way of updating list and printing to screen nicely at each step"""
    times = []

    def update(self, i, j, n):
        self.times.append(i)
        print('+ collect {} chefs at time {}'.format(discharge(i, j, n), i))


def charge(j):
    """charge is a exponential function of j"""
    return(j**2)


def discharge(i, j, n):
    """
    calculates the number of chefs that can be processed at [i,j].
    """
    return(min(charge(j), n[i]))


def optimize(n):

    k = len(n)
    schedule = np.zeros((k+1, k+1)) # k+1 set to zero for base case
    times = Times()

    # i = time step, j = charge level (starting with 0 charge)
    for i in range(k-1 , -1, -1):
        for j in range(i, -1, -1):

            # if we discharge now, we gain min(charge(j), n[i]) 
            # as well as the number of chefs from the next time
            # step [i+1] -- but we has no charge
            discharge_now = discharge(i, j, n) + schedule[i+1, 0]    

            # dont discharge: take the chefs computed at the next hour
            discharge_next = schedule[i+1, j+1]

            # we take the maximum of these two
            schedule[i, j] = max(discharge_now, discharge_next)

    max_chefs = int(schedule[0, 0])


    # traverse the schedule to find the optimal battery discharge times 
    # starting from [0,0]. We always search the matrix diagonally. When we
    # discharge, we reset j to 0, but continue searching diagonally.

    j = 0
    for i in range(k):

        # if [i, j] == [i+1, j+1], nothing changed at this step so we increment
        if schedule[i, j] == schedule[i+1, j+1]:
            j += 1
            continue

        # if [i, j] == [i+1, 0] + the discharge value of [i, j], we must
        # have discharged at i. set j to zero and continue diagonally
        elif schedule[i, j] == schedule[i+1, 0] + discharge(i, j, n):
            times.update(i, j, n)
            j = 0

    # if the final value we rest on is also not empty, add it
    # we have schedule[i, j] != schedule[i-1, j-1] to prevent double-
    # counting a person (due to the j += 1 on line 59).
    if schedule[i, j] != 0 and schedule[i, j] != schedule[i-1, j-1]:
        times.update(i, j, n)       

    return(max_chefs, schedule, times.times)

# contains the number of chefs available at each i
print('---time-a tu meke-a sume-a testy cuocuomber---\n')

k = 10
n = np.random.randint(0, 20, k)
n_chefs, schedule, times = optimize(n)

print('+ n_chefs: {} at {}\n\n{}\n\n+ full schedule={}'.format(
    n_chefs, times, schedule, n))
