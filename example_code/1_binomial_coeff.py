import math

n_recursion = 0
def recursion(n, k):
    global n_recursion
    n_recursion += 1
    if k == 0 or k == n:
        return 1
    else:
        return recursion(n-1, k-1) + recursion(n-1, k)

def mathematical(n, k):
    return math.factorial(n)/math.factorial(n-k)/math.factorial(k) 

n_pascal = 0
def pascal_triangle(n, k): # dynamic programming
    global n_pascal
    C = [[0 for x in range(k+1)] for y in range(n+1)]

    for i in range(0, n+1):
        C[i][0] = 1
        n_pascal += 1 
        for j in range(1, min(i,k)+1):
            C[i][j] = C[i-1][j-1] + C[i-1][j]
            n_pascal += 1 

    return C[n][k]

n = 10
k = 5
print mathematical(n, k)
print recursion(n, k), 'n_recursion: {}'.format(n_recursion)
print pascal_triangle(n, k), 'n_pascal: {}'.format(n_pascal)
