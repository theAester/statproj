import networkx as nx
import matplotlib.pyplot as plt
import scipy
from numpy.random import randint
from numpy.random import rand
import numpy as np
from real import genReal
from make import makeGraph
###################################
############see s14.py#############
###################################
n= 150
p = 0.2
m = 3000
X = np.linspace(10,150,15)
print(X)
Y=[]
Z=[]
for x in X:
    S = 0
    H = 0
    for i in range(100):
        G = makeGraph(int(x),4/x) #same as s14.py but p = 4/n
        c = nx.number_connected_components(G) 
        if c == 1:
            H+=1
        for j in range(int(x)):
            if G.degree[j] == 0:
                S+=1
                break
    H/=100
    S/=100
    Y.append(S)
    Z.append(H)
_,ax = plt.subplots()
ax.plot(X,Y)
ax.plot(X,Z)
ax.legend(["P[stray]", "P[connected]"])
plt.show()
