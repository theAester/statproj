import networkx as nx
import matplotlib.pyplot as plt
import scipy
from numpy.random import randint
from numpy.random import rand
import numpy as np
from real import genReal
from make import makeGraph

def diameter(G): #find the maximum diameter among all connected components
    maxdim = 0
    V = [G.subgraph(c).copy() for c in nx.connected_components(G)]
    for v in V:
        r = nx.diameter(v) #built-in algorithm to calculate diameter
        if r > maxdim :
            maxdim = r
    return maxdim

n= 50
p = 0.34
m = 3000

S=0
for i in range(100):
    G = makeGraph(n,p)
    L = diameter(G) #calculate diameter
    S+=L #accumulate diameter

print(S/100) #average
				
	
