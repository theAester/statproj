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
    G = makeGraph(n,p)
    for j in range(n):
        if G.degree[j] == 0:
            S+=1
            break
print(S/100)
