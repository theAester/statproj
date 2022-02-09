import networkx as nx
import matplotlib.pyplot as plt
import scipy
from numpy.random import randint
from numpy.random import rand
import numpy as np
from real import genReal
from make import makeGraph

n= 1000
p = 0.033
m = 3000

G = makeGraph(n,p)

D = nx.floyd_warshall(G) #algorithm to find the minimum distance between all pairs of nodes
S=0
for i in range(n): #iterate through all
	for j in range(i+1,n):
		#print(D[i][j])
		S += D[i][j] #add
S = S/(n*(n-1)/2) #average

print(S)
				
#nx.draw(G, with_labels=True)
#plt.show()	
	
