import networkx as nx
import matplotlib.pyplot as plt
import scipy
from numpy.random import randint
from numpy.random import rand
def genReal(n,m):
    REAL = nx.Graph()
    for i in range(m):
        l1 = randint(0,n);
        l2 = randint(0,n);
        if(l1 == l2):
            l2= (l2+randint(0,n/2)) % n 
        G.add_edge(l1,l2);
    return REAL

