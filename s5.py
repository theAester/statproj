import networkx as nx
import matplotlib.pyplot as plt
import scipy
from numpy.random import randint
from numpy.random import rand
from real import genReal
from make import makeGraph

n= 1000
p = 0.003
m = 3000

JFF = 0

G = makeGraph(n,p)
FF = 0
for i in range(n):
	N = list(G.neighbors(i)) #list of neighbors
	nn = len(N) #same as G.degree[i]
	for j in range(nn): #iterate through all 2-choices of neighbors
		for k in range(j+1,nn):
			if(G.has_edge(N[j],N[k])): #if theres an edge add to FF
				FF+=1
FF/=n #average of FF
print(FF)
	
	
