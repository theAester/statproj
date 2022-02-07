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
X = np.linspace(10,150,15)
print(X)
Y=[]
for x in X:
    S = 0
    for i in range(100):
        G = makeGraph(int(x),4*np.log(x)/x)
        for j in range(int(x)):
            if G.degree[j] == 0:
                S+=1
                break
    S/=100
    Y.append(S)
_,ax = plt.subplots()
ax.plot(X,Y)
plt.show()
