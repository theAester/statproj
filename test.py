import networkx as nx
import matplotlib.pyplot as plt
import scipy
from numpy.random import randint
from numpy.random import rand
from real import genReal
from make import makeGraph

G = nx.Graph()
G.add_edge(1,2)
G.add_edge(1,3)
print(G[2][3])
