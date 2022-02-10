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
X = np.linspace(10,150,15) #list of values of n
Y=[] #for plotting P[stray]
Z=[] #for plotting P[connected]
for x in X:
    S = 0.0
    H = 0.0
    for i in range(100):
        G = makeGraph(int(x),4*np.log(x)/x)
        c = nx.number_connected_components(G) 
        if c == 1:
            H+=1
        for j in range(int(x)):
            if G.degree[j] == 0:
                S+=1
                break
    H/=100
    S/=100 #same as 213.py
    Y.append(S) #add to y-axis values
    Z.append(H)
_,ax = plt.subplots()
ax.plot(X,Y) 
ax.plot(X,Z) #plot
ax.legend(["P[stray]", "P[connected]"])
plt.show()
