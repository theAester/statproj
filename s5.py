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
	N = list(G.neighbors(i))
	nn = len(N)
	for j in range(nn):
		for k in range(j+1,nn):
			if(G.has_edge(N[j],N[k])):
				FF+=1
FF/=n
print(FF)
	
	
