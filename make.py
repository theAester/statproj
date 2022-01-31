import networkx as nx
import matplotlib.pyplot as plt
import scipy
from numpy.random import randint
from numpy.random import rand
def makeGraph(n,p):
    MADE = nx.Graph()
    MADE.add_nodes_from(range(n));
    for i in range(n):
        for j in range(i+1,n):
            if rand() < p :
                MADE.add_edge(i,j)
    return MADE
