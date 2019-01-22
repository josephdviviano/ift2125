#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 21:35:21 2018

@author: marziehmehdizadeh
"""

#devide an integer in 4 equal parts as much as possible
def get_ind4(n):
    if n%4==0:
        list_ind=[n//4,n//2,3*n//4,n]
    elif n%4==1:
        list_ind=[(n-1)//4,(n-1)//2,3*(n-1)//4,n]
    elif n%4==2:
        list_ind=[(n-2)//4,(n-2)/2,3*(n-2)//4+1,n]
    else:
         list_ind=[(n-3)//4,(n-3)//2+1,3*(n-3)//4+2,n]
         
    return(list_ind)


def merge4(l1,l2,l3,l4):
    n1=len(l1)
    n2=len(l2)
    n3=len(l3)
    n4=len(l4)
    r=100000
    i1=0
    i2=0
    i3=0
    i4=0
    l_sorted=[]
    while i1<n1 or i2<n2 or i3<n3 or i4<n4:
        find_min=[]
        if i1<n1:
            find_min.append(l1[i1])
        else:
            find_min.append(r)
        if i2<n2:
            find_min.append(l2[i2])
        else:
            find_min.append(r)
        if i3<n3:
            find_min.append(l3[i3])
        else:
            find_min.append(r) 
        if i4<n4:
            find_min.append(l4[i4])
        else:
            find_min.append(r)   
        val, idx = min((val, idx) for (idx, val) in enumerate(find_min))
        l_sorted.append(val)
        if idx==0:
            i1=i1+1
        if idx==1:
            i2=i2+1
        if idx==2:
            i3=i3+1
        if idx==3:
            i4=i4+1
    return l_sorted    

def mergsort4(A):
    n=len(A)
    if n<=3:
        return sorted(A)
    else:
        list_of_ind=get_ind4(n)
        
        i0=list_of_ind[0]
        i1=list_of_ind[1]
        i2=list_of_ind[2]
        i3=list_of_ind[3]
        print(i0,i1,i2,i3)
        l1=A[0:i0]
        l2=A[i0:i1]
        l3=A[i1:i2]
        l4=A[i2:i3]
        sl1=mergsort4(l1)
        sl2=mergsort4(l2)
        sl3=mergsort4(l3)
        sl4=mergsort4(l4)
        merged_list=merge4(sl1,sl2,sl3,sl4)
        return merged_list      