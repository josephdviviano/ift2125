
# coding: utf-8

# # TP 6 - 16 février 2018
# ## Par Stéphanie Larocque

# In[7]:


import numpy as np


# ## Question 2
# 
# ### Implémenter l'algorithme de Prim 1 - de façon "bête" et 2 - de façon intelligente

# In[8]:


def prim(n, E):
    n = len(V)
    E = sorted(E, key = lambda elem:elem[1])
    T = []
    B = {V[0]}
    
    
    # At each step, we will select the smallest adjacent edge to the set of already considered vertices B
    # We go through all the edges and stop when we find an edge (u,v) s.t. u is in B and v isn't (or vice versa)
    # We thus add the (u,v) edge to the tree and update B by adding u or v
    while len(B)!=n:                                   
        for (u,v), poids in E: # Car E reste sorted tout au long...
            if (u in B)!=(v in B):
                break
        T.append([(u,v), poids])
        E.remove([(u,v), poids])
        B.update([u,v]) # same as B.add(u) and B.add(v)
    return T


# In[9]:


from heapq import heappush, heappop

def prim_heap(V, E):
    x = V[0] #arbitrary vertex
    n = len(V)
    T = [] # Tree in construction (edges)
    B = {x} # Vertices in the tree T
    H = [] # Heap containing "sorted" edges adjacent to >= 1 vertex of B
    
    # Liste des voisins pour chaque sommet
    voisins = [[] for i in range(n)]
    for (u,v), poids in E:
        voisins[u].append((v, poids))
        voisins[v].append((u, poids))
    
    
    while len(B)!=n :
        for (v, poids) in voisins[x]:
            heappush(H, (poids, (x,v)))
        
        # Find minimum weight edge in H that does not create a cycle
        poids, (u,v) = heappop(H) #remove and return smallest element in H
        while (u in B) and (v in B) :
            poids, (u,v) = heappop(H)
        
        # The edge (u,v) will the smallest edge with 1 vertex in B and the other not in B
        T.append([(u,v), poids])
        x = u if v in B else v
        B.add(x)
    return T
        
    
    
    


# In[10]:


V = [0,1,2,3,4,5,6]
E = [[(0, 1), 1], [(1, 2), 2], [(3, 4), 3], [(5, 6), 3], 
     [(0, 3), 4], [(1, 4), 4], [(3, 6), 4], [(2, 4), 5],
     [(1, 3), 6], [(2, 5), 6], [(4, 6), 7], [(4, 5), 8]]
    
print(E)
print("----------Prim sans heap---------------")
T = prim(V, E)
for (u,v), poids in T:
    print("Arete", str(u)+"-"+str(v), "poids", poids)
print("----------Prim avec heap---------------")
T = prim(V, E)
for (u,v), poids in T:
    print("Arete", str(u)+"-"+str(v), "poids", poids)

