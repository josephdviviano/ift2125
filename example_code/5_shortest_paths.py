import math

inf = float('Inf')

def floyd(L):
  n = len(L)
  
  # init a matrix
  D = [[L[j][i] for i in range(n)] for j in range(n)] 
  P = [[None for i in range(n)] for j in range(n)] 

  for k in range(n):
    for i in range(n):
      for j in range(n):
        #D[i][j] = min(D[i][j], D[i][k] + D[k][j])
        if D[i][j] > D[i][k] + D[k][j]:
          D[i][j] = D[i][k] + D[k][j]
          P[i][j] = k
    print 'k: {}'.format(k)
    print 'D: ', D
    print 'P: ', P 
    print ''

  return D

# example
# (vertext index starts from 0)
L = [[0, 5, inf, inf],
     [50, 0, 15, 5],
     [30, inf, 0, 15],
     [15, inf, 5, 0]]
print 'L: ', L
print ''
print floyd(L)
