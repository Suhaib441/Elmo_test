#!/usr/bin/env python
# coding: utf-8

# In[458]:


from elmoformanylangs import Embedder
from scipy.spatial import distance
import numpy as np
import math
from itertools import combinations 


# In[460]:


e = Embedder('./150') #l'importation du modèle 


# In[461]:


sents = ['souris','mulot','escargot','chaise']

h=e.sents2elmo(sents) #la transformation en vecteur 


# In[ ]:





# In[ ]:





# In[ ]:





def ecludienne(vector1, vector2):
    ''' on utilise scipy pour calcuer la distance ecludienne. '''
    if vector1.shape == vector2.shape: 
        a=vector1.flatten() #transformation en vecteurs de 1D au lieu de 2D 
        b=vector1.flatten()
        dist = distance.euclidean(a, b) # distance 
        
        #dist = [(un - deux)**2 for un, deux in zip(vector1, vector2)]
        #dist = math.sqrt(sum(dist))
    else: 
        #Les deux vecteurs peuvent avoir differentes taills, et pour pouvoir calculer la distance faut que les vecteurs aient la même taille
        long=len(vector1)
        long2=len(vector2)
        diff=abs(long-long2) #la difference de taille entre les 2 vecteurs 
        if vector1.shape < vector2.shape:
            array_diff=np.zeros([diff,vector1.shape[1]])# m c'est les la difference en arrays 
            vector1=np.vstack((vector1, array_diff)) #ajout des rows de 0 pour avoir la même taille 

            a=vector1.flatten()
            b=vector2.flatten()
            dist = distance.euclidean(a, b)
        
        elif vector1.shape > vector2.shape:
            array_diff=np.zeros([diff,vector1.shape[1]])
            vector2=np.vstack((vector2, array_diff))

            a=vector1.flatten()
            b=vector2.flatten()
            dist = distance.euclidean(a, b)
            #SI on veut utiliser NUmpy
            #dist = [(un - deux)**2 for un, deux in zip(vector1, vector2)]
            #dist = math.sqrt(sum(dist))
    return dist









def comparison(l):
        distance_ecludienne=[] 
        for i,k in zip(combinations(l, 2),combinations(sents,2)): #pour avoir une combinaison 2vs2 & la distance
            distance_ecludienne.append((k[0],k[1],ecludienne(i[0],i[1])))
        return distance_ecludienne





dis=comparison(h)
cmpt=1
for i in dis:
        print("{}- {} - {} \n ont une distance ecludienne de {}".format(cmpt,i[0],i[1], i[2]))
        cmpt+=1


