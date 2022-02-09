import networkx as nx
import matplotlib.pyplot as plt
import scipy
from numpy.random import randint
from numpy.random import rand
def makeGraph(n,p):
    return nx.fast_gnp_random_graph(n, p)
