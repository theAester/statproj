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
    A = nx.adjacency_matrix(G).todense().tolist() #adjacency matrix as a standard 2-d array
    A2 = np.matmul(A,A) #matrix multipication to get A^2(time-complexity depeds on system's BLAS but its typically O(n^2.37))
    tr = 0
    for j in range(n):
        for k in range(n): #multiply A2 by A and only calculate the elements on the main diameter O(n^2)
            tr += A2[j][k]*A[k][j] #accumulate values to find trace of A^3
    tr /= 6 #number of triabngles(well -known formula: number of k-loops = tr(A^k)/k! where A is the adjacency matrix)
    T += tr #accumulate number of triangles
T /= 100 #average number of triangles
print(T) #total time complexity O(100*r(n^2.37) (r is time-complexity of networkx makeGraph(unknown))
