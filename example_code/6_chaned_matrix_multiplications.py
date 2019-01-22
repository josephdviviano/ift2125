import math

inf = float('Inf')


def count_matrix_multiplications(d):
  # d: dimensions of matrices d_0, ..., d_n-1, d_n
  #    each matrix M_i = d_i-1 x d_i matrix for i = 1, ..., n
  n = len(d)

  # init a matrix
  M = [[inf for i in range(n)] for j in range(n)]

  # base case s = 0
  s = 0
  for i in range(1, n-s):
    j = i+s
    M[i][j] = 0
  print 's: {}'.format(s)
  print M 

  # base case s = 1
  s = 1
  for i in range(1, n-s):
    j = i+s
    for k in range(i, j): # from i to j, (j-i) == s
      M[i][j] = d[i-1]*d[k]*d[j]
  print 's: {}'.format(s)
  print M 

  # other cases
  for s in range(2,n):
    for i in range(1, n-s):
      j = i+s
      for k in range(i, j): # from i to j, (j-i) == s
        M[i][j] = min(M[i][j], M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j])
    print 's: {}'.format(s)
    print M 

  print M 
  return M[1][-1]

# example
d = [13, 5, 89, 3, 34]
print count_matrix_multiplications(d)
