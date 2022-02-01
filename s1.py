import networkx  as nx
import numpy as np
n = 1000
p = 0.0034
m = 3000
thereshold = 0.05
A = []
def graph_generator(n,p,A):
    s = 0
    G = nx.fast_gnp_random_graph(n, p)
    s += G.number_of_edges()
    A.append(s)

def accuracy_formula(A, m, thereshold):
    if abs(m - np.sum(A)/10) <= thereshold*m:
        return print("m and excpected value are equal with 5 percent thereshold")
    else:
         return print("m and excpected value are not equal with 5 percent thereshold")



for i in range(0,10):
    graph_generator(n,p,A)

print(np.sum(A)/10)
print(A) 
accuracy_formula(A, m, thereshold)
