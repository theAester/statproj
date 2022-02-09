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
	T = 0 #tora gozari...
	R = 0 #reghabat
	for i in range(n): #O(n*DELTA^2) ; DELTA ~ 2*n*p
		N = list(G.neighbors(i)) # list of edge i's neighbors
		nn = len(N) #same as G.degree[i]
		for j in range(nn):
			for k in range(j+1,nn): #iterate through all 2-choices of i's neighbors
				if(G.has_edge(N[j],N[k])): #if they have an edge then its a triangle(tora gozari...)
					T+=1
				else: #if not its a cherry (reghabat)
					R+=1
	T/=3 # each triangle is counted 3 times
	JT += T #accumulate the number of triangles
	JR += R #accumulate the number of cherries
JT/=5 #average
JR/=5 #average
print(f"Triabgles={JT}\nCherries={JR}")
	
	
