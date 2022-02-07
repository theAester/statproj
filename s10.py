import networkx as nx
import matplotlib.pyplot as plt
import scipy
from numpy.random import randint
from numpy.random import rand
import numpy as np
from real import genReal
from make import makeGraph

n= 100
p = 0.34
m = 3000
X = np.linspace(10,100,10)
print(X)
Y=[]
for x in X:
    T = 0
    for i in range(100):
        G = makeGraph(int(x),60/(x*x))
        A = nx.adjacency_matrix(G).todense().tolist()
        A2 = np.matmul(A,A)
        tr = 0
        for j in range(int(x)):
            for k in range(int(x)):
                tr += A2[j][k]*A[k][j]
        tr /= 6
        T += tr
    T /= 100
    Y.append(T)
_,ax = plt.subplots()
ax.plot(X,Y)
plt.show()
print(T)
