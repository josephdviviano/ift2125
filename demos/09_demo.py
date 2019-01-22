
# coding: utf-8

# # Demo 9 - 6 avril 2018
# 
# ## Stéphanie Larocque

# In[1]:


import numpy as np


# ## Question 1 : Tri topologique d'un graphe orienté acyclique par parcours en profondeur.

# In[12]:


def tri_topo(G):
    # Input G = (V, E) a graph.
    # Output sorted list in topological order of the vertices 
    V, E = G
    
    # Find the roots (vertices with no parents) of the directed acyclic graph
    parents= {v:set() for v in V} 
    for (u1,u2) in E:
        parents[u2].add(u1)
    roots=[v for v in V if parents[v]==set()]
    
    # Start a DFS for each root
    label = {v:0 for v in V} # label[v] = 1 when visited (i.e. when all its children are visited as well), otherwise 0
    sorted_list = []
    for r in roots:
        sorted_list = DFS_topo(G, r, [], label) + sorted_list
    
    return sorted_list
        


# In[13]:


def DFS_topo(G, u, sorted_list, label):
    # Input : graph G = (V,E)
    #         vertex u
    #         sorted list
    #         array of label (label[v]=1 when visited, 0 otherwise)
    
    V, E = G
    label[u] = 1
    
    # Parcours en profondeur du graphe afin de rajouter les sommets a la liste triée.
    sorted_list = []
    for (u1, u2) in E:
        if u1==u and label[u2]==0:
            sorted_list = DFS_topo(G, u2, sorted_list, label) + sorted_list
    

    return [u] + sorted_list


# In[14]:


V = [0, 1, 2, 3, 4, 6, 12, 8, 24]
E = [(0,2),(1,2), (1,3), (2,4), (2,6), (3, 6), (4, 12), (4, 8), (6,12), (8,24), (12, 24)]
G = (V, E)

liste_triee = tri_topo(G)
print(liste_triee)


# ## Question 4 : Distance d'édition de mots u et v

# In[5]:


def make_table_DP(u,v):
    n = len(u)
    m = len(v)
    T = np.zeros((n+1, m+1))
    
    for i in range(n+1):
        T[i,0] = i
    for j in range(m+1):
        T[0,j] = j
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            suppression = T[i-1, j] + 1
            insertion = T[i, j-1] + 1
            delta_ij = 0 if u[i-1]==v[j-1] else 1 # string indicées à 0
            substitution = T[i-1, j-1] + delta_ij      
            T[i][j] = min(suppression, insertion, substitution)
    return T
    


# In[6]:


def distance_edition(u,v):
    T = make_table_DP(u,v)
    return T[-1][-1]


# In[7]:


def find_alignment(u,v):
    # Retourne 1 alignement optimal
    # Possible qu'il y en ait plusieurs
    
    T = make_table_DP(u,v)
    i = len(u)
    j = len(v)
    
    solu_u = ""
    solu_v = ""
    
    while i>0 or j>0:
        
        suppression = T[i-1, j] + 1
        insertion = T[i, j-1] + 1
        delta_ij = 0 if u[i-1]==v[j-1] else 1 # string indicées à 0
        substitution = T[i-1, j-1] + delta_ij
        
        if T[i,j] == suppression :
            i-=1
            solu_u = u[i] + " " + solu_u
            solu_v = "- " + solu_v
            
            
        elif T[i,j] == insertion :
            j-=1
            solu_u = "- " + solu_u
            solu_v = v[j] + " " + solu_v
        
        elif T[i,j] == substitution:
            i-=1
            j-=1
            solu_u = u[i] + " " + solu_u
            solu_v = v[j] + " " + solu_v
    
    return solu_u, solu_v
            
            


# In[8]:


u = "ACTGGGCTA"
v = "GTAACTGA"
distance_edition(u, v)


# In[9]:


print("-------Mots-------")
print("u =", u)
print("v =", v)
print("------Alignement optimal-------")
sol_u, sol_v = find_alignment(u,v)
print("u:",sol_u)
print("v:",sol_v)


# In[10]:


u = "bonjour"
v = "journee"
distance_edition(u, v)

print("------Alignement optimal-------")
sol_u, sol_v = find_alignment(u,v)
print("u:",sol_u)
print("v:",sol_v)


# In[11]:


u = "table"
v = "stage"
distance_edition(u, v)

print("------Alignement optimal-------")
sol_u, sol_v = find_alignment(u,v)
print("u:",sol_u)
print("v:",sol_v)

