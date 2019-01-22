'''
Exemplaires.py

Author: Dendi Suhubdy and Jae Hyun Lim
'''


def product(tuple1, tuple2):
    result = tuple(tuple2[tuple1[i] - 1] for i in range(len(tuple1)))
    return result

def inverse(tuple_to_inverse):
    inverse_result = [0] * len(tuple_to_inverse)
    for i in xrange(tuple_to_inverse):
        inverse_result[tuple_to_inverse[i]-1] = i + 1
    return inverse_result

def composition(permutation, r):
    ID = tuple(range(1, len(r)+1))
    stopping_condition = [(p, q) for p in permutation for q in permutation]

    while len(stopping_condition)>0:
        (p, q) = stopping_condition.pop()
        z = product(p,q)
        #print(str(p) + ' o ' + str(q))
        '''
        if z in permutation:
            print('already have it')
        else:
        '''
        if not(z in permutation):
             stopping_condition.extend([(p, z) for p in permutation])
             stopping_condition.extend([(z, p) for p in permutation])
             permutation.add(z)
             #print('=')
             #print(z)
             #print('\n')
             if z==r:
                 return True
    print('False')
    return r in permutation

def main():
    f11 = tuple([3, 1, 3, 4])
    f12 = tuple([3, 4, 2, 1])
    s1 = set([f11,f12])
    f1 = tuple([1, 1, 1, 2])

    f21 = tuple([3, 5, 4, 2, 6, 8, 1, 7])
    f22 = tuple([1, 4, 3, 2, 5, 6, 7, 8])
    s2 = set([f21,f22])
    f2 = tuple([8, 7, 6, 5, 4, 3, 2, 1])

    f31 = tuple([3, 3, 4, 4, 5, 5])
    f32 = tuple([3, 4, 2, 1, 6, 6])
    f33 = tuple([4, 4, 4, 4, 5, 5])
    s3 = set([f31,f32,f33])
    f3 = tuple([2, 1, 4, 3, 5, 5])

    f41 = tuple([1, 2, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    f42 = tuple([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1])
    f43 = tuple([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    s4 = set([f41,f42,f43])
    f4 = tuple([2, 1, 4, 3, 5, 7, 7, 7, 7, 7, 7, 7])

    f51 = tuple([3, 3, 5, 5, 7, 7, 1, 1, 11, 12, 12, 1])
    f52 = tuple([3, 3, 1, 1, 5, 5, 7, 7, 7, 4, 12, 11])
    f53 = tuple([1, 1, 3, 3, 5, 5, 9, 7, 9, 9, 10, 12])
    s5 = set([f51,f52,f53])
    f5 = tuple([7, 7, 3, 3, 1, 1, 5, 5, 12, 11, 10, 4])

    f61 = tuple([3, 4, 4, 2, 6, 8, 1, 7, 3])
    f62 = tuple([4, 4, 4, 4, 4, 5, 5, 8, 1])
    s6 = set([f61,f62])
    f6 = tuple([2, 1, 4, 4, 5, 6, 8, 7, 3])

    '''
    Conduct operations of exemplaire
    '''

    print('composition(s1,f1)')
    print(composition(s1,f1))

    print('composition(s2,f2)')
    print(composition(s2,f2))

    print('composition(s3,f3)')
    print(composition(s3,f3))

    print('composition(s4,f4)')
    print(composition(s4,f4))

    print('composition(s5,f5)')
    print(composition(s5,f5))

    print('composition(s6,f6)')
    print(composition(s6,f6))

if __name__=="__main__":
    main()
