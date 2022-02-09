import networkx as nx
import matplotlib.pyplot as plt
import scipy
from numpy.random import randint
from numpy.random import rand
import numpy as np
from real import genReal
from make import makeGraph

n= 150
p = 0.2
m = 3000
S = 0.0
for i in range(100):
    G = makeGraph(n,p) #make graph
    for j in range(n): #iterate through degree of nodes
        if G.degree[j] == 0: #if a node is stray 
            S+=1 #add to number of strays 
            break #and make the graph again
print(S/100) #average the number of graphs with a stray node
