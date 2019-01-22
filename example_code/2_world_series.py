import math

p = 0.5
q = 1 - p
n = 4 

def recursion(i, j):
  if i == 0 and j == 0:
    return None
  elif i == 0:
    return 1.
  elif j == 0:
    return 1.
  else:
    return p * recursion(i-1, j) + q * recursion(i, j-1)

# a prob of team A win given that A need i more victories and B need j more.
def dc(n, p):
  q = 1-p
 
  P = [[0 for i in range(n+1)] for j in range(n+1)]

  # P(0, 0) = None
  P[0][0] = None

  for s in range(1, n+1):
    P[0][s] = 1
    P[s][0] = 0
    for k in range(1, s):
      P[k][s-k] = p * P[k-1][s-k] + q * P[k][s-k-1]

  for s in range(1, n+1):
    for k in range(n-s+1):
      P[s+k][n-k] = p * P[s+k-1][n-k] + q * P[s+k][n-k-1]

  ## P(0, j) = 1 for all i
  #for j in range(1, n+1):
  #  P[0][j] = 1.

  ## P(i, 0) = 1 for all i
  #for i in range(1, n+1):
  #  P[i][0] = 1.

  #for i in range(1, n+1):
  #  for j in range(1, n+1):
  #    P[i][j] = p * P[i-1][j] + q * P[i][j-1]

  return P[-1][-1]

#print recursion(2,2)
print recursion(4,4)
print dc(4,4)
