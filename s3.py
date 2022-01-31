import networkx as nx
import matplotlib.pyplot as plt
import scipy
from numpy.random import randint
from numpy.random import rand
from real import genReal
from make import makeGraph

n= 3000
p = 0.01
m = 3000

JT = 0
JR = 0
for s in range(5):
	G = makeGraph(n,p)
	T = 0
	R = 0
	for i in range(n):
		N = list(G.neighbors(i))
		nn = len(N)
		for j in range(nn):
			for k in range(j+1,nn):
				if(G.has_edge(N[j],N[k])):
					T+=1
				else:
					R+=1
	T/=3
	JT += T
	JR += R
JT/=5
JR/=5
print(f"{JT}\n{JR}")4533
	
	
