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

T = 0
for i in range(100):
    G = makeGraph(n,p)
    A = nx.adjacency_matrix(G).todense().tolist()
    A2 = np.matmul(A,A)
    tr = 0
    for j in range(n):
        for k in range(n):
            tr += A2[j][k]*A[k][j]
    tr /= 6
    T += tr
T /= 100
print(T)
