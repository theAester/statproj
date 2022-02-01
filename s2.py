import networkx as nx
import matplotlib.pyplot as plt
import scipy
from numpy.random import randint
from numpy.random import rand
from real import genReal
from make import makeGraph
import numpy as np

n= 1000
p = 0.00016
m = 3000

J = 0
Y=[]
for s in range(10):
    G = makeGraph(n,p)
    #makeGraph is a fucntion from make that make a random graph with n nodes and with probability of p
    v = 0
    for i in range(n):
        Y.append(G.degree[i])
        v+= G.degree[i]
    L = v/n
    for i in range(n):
    	if(G.degree[i] > L):
    		J+=1
            
_,ax = plt.subplots()
ax.hist(Y)
J/=10
print(J)
plt.show()


	
