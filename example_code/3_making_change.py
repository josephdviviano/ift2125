import math

inf = float('Inf')

def coins(d, N):
    # number of units
    n = len(d)

    # set up table
    c = [[0 for i in range(N+1)] for j in range(n)]

    # run dynamic programming
    for i in range(n):
      for j in range(1, N+1):
        if i-1 < 0:
          c_no_add = inf
        else:
          c_no_add = c[i-1][j]

        if j-d[i] < 0:
          c_add = inf 
        else:
          c_add = c[i][j-d[i]]

        #print i, j, c_no_add, c_add + 1
        c[i][j] = min(c_no_add, c_add + 1)

    print c
    return c[n-1][N-1]

# coins
d = [1, 4, 6]
N = 8 # the target change

print coins(d, N)
