import math

inf = float('Inf')

def knapsack(w, v, W):
  # number of items
  n = len(v)
 
  V = [[0 for i in range(W+1)] for j in range(n)]

  for i in range(n):
    for j in range(1, W+1):
      if i-1 < 0:
        v_no_add = -inf
      else:
        v_no_add = V[i-1][j]

      if j-w[i] < 0:
        v_add = -inf
      else:
        v_add = V[i-1][j-w[i]] + v[i]

      V[i][j] = max(v_no_add, v_add)

  print V
  return V[n-1][W]

W = 11 
w = [1, 2, 5, 6, 7]
v = [1, 6, 18, 22, 28]
#ind = [0, 4, 1, 3, 2]
#w = [w[i] for i in ind]
#v = [v[i] for i in ind]
print knapsack(w, v, W)
