import networkx as nx
import matplotlib.pyplot as plt
import scipy
from numpy.random import randint
from numpy.random import rand
from real import genReal
from make import makeGraph

n= 1000
p = 0.00016
m = 3000

J = 0
for s in range(10):
    G = makeGraph(n,p)
    v = 0
    for i in range(n):
    	v+= G.degree[i];
    L = v/n
    print(L)
    for i in range(n):
    	if(G.degree[i] > L):
    		J+=1
J/=10
print(J)
	
	
