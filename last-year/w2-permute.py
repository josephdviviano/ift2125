def product(p, q):
    return tuple(q[p[i]-1] for i in range(len(p)))

print product((2,3,4,5,1), (2,1,3,4,5)) 

def inverse(p):
   q = [0] * len(p)
   for i in range(len(p)):
      q[p[i]-1] = i+1
   return tuple(q)

print ''
print (2, 1, 3, 4, 5)
print inverse((2, 1, 3, 4, 5))
print product(inverse((2, 1, 3, 4, 5)), (2, 1, 3, 4, 5))
print product((2, 1, 3, 4, 5), inverse((2, 1, 3, 4, 5)))

def sift(tableau, p):
   IDENTITY = tuple(range(1, len(p)+1))
   q=p
   while q != IDENTITY:
     i = min(x for x in range(len(q)) if q[x] != x+1)
     j = q[i] - 1
     if tableau[i][j] == IDENTITY:
        tableau[i][j] = q
        return q
     else:
        q = product(q, inverse(tableau[i][j]))
   return None

def print_table(tableau):
    for i in range(len(tableau)):
        print tableau[i]

print ''
a = (2, 1, 3, 4, 5) # (12)(3)(4)(5)
b = (2, 3, 4, 5, 1) # (12345)
r = (3, 2, 4, 5, 1) #(1345)
IDENTITY = tuple(range(1, len(r)+1))
tableau = [[IDENTITY] * len(r) for _ in range(len(r))]
print IDENTITY
print ''
print_table(tableau)
print ''
print sift(tableau, a)
print_table(tableau)
print ''
print sift(tableau, b)
print_table(tableau)

def get_permutes(tableau, IDENTITY):
    return [tableau[i][j] for i in range(len(tableau[0])) for j in range(len(tableau[0][0])) if tableau[i][j] != IDENTITY]

print get_permutes(tableau, IDENTITY)

def appartenance_intelligent1(permutations, r):
    IDENTITY = tuple(range(1, len(r)+1))
    tableau = [[IDENTITY] * len(r) for _ in range(len(r))]
 
    # Tamisage initial / Initial sift
    for p in permutations:
        sift(tableau, p)

    # Remplir tableau / Fill table
    to_sift = [(p, q) for p in permutations for q in permutations]
    while len(to_sift) > 0:
        p, q = to_sift.pop()
        q = sift(tableau, product(p, q))
        if q is not None:
        # q est une nouvelle permutation ajoutee au tableau
            to_sift.extend([(p, q) for p in permutations])
            to_sift.extend([(q, p) for p in permutations])
    # Genere r? / Generates r?
    #print_table(tableau)
    print get_permutes(tableau, IDENTITY)
    return sift(tableau, r) is None

def appartenance_intelligent2(permutations, r):
    IDENTITY = tuple(range(1, len(r)+1))
    tableau = [[IDENTITY] * len(r) for _ in range(len(r))]
 
    # Tamisage initial / Initial sift
    for p in permutations:
        sift(tableau, p)

    # Remplir tableau / Fill table
    to_sift = [(p, q) for p in get_permutes(tableau, IDENTITY) for q in get_permutes(tableau, IDENTITY)]
    while len(to_sift) > 0:
        p, q = to_sift.pop()
        q = sift(tableau, product(p, q))
        if q is not None:
        # q est une nouvelle permutation ajoutee au tableau
            to_sift.extend([(p, q) for p in get_permutes(tableau, IDENTITY)])
            to_sift.extend([(q, p) for p in get_permutes(tableau, IDENTITY)])
    # Genere r? / Generates r?
    #print_table(tableau)
    print get_permutes(tableau, IDENTITY)
    return sift(tableau, r) is None


# Exemple / Example
print ''
a = tuple([2, 1, 3, 4, 5]) # (12)(3)(4)(5)
b = tuple([2, 3, 4, 5, 1]) # (12345)
r = tuple([2, 1, 4, 5, 3]) # (12)(345)

print 'Example1: r in <a, b>?'
print 'a: ', a
print 'b: ', b 
print 'r: ', r 
print(appartenance_intelligent1(set([a,b]), r))
print(appartenance_intelligent2(set([a,b]), r))


# Exemple / Example
print ''
a = tuple([2, 1, 3, 4, 5]) # (12)(3)(4)(5)
b = tuple([2, 3, 1, 4, 5]) # (123)(45)
r = tuple([2, 5, 4, 3, 1]) # (125)(34)

print 'Example2: r in <a, b>?'
print 'a: ', a
print 'b: ', b 
print 'r: ', r 
print(appartenance_intelligent1(set([a,b]), r))
print(appartenance_intelligent2(set([a,b]), r))


# Exemple / Example
print ''
b = tuple([2, 3, 4, 5, 1]) # (12345)
r = tuple([2, 1, 4, 5, 3]) # (12)(345)

print 'Example3: r in <b>?'
print 'b: ', b 
print 'r: ', r 
print(appartenance_intelligent1(set([b]), r))
