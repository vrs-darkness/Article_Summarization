import networkx as nx
import numpy as np

def Model(X,sentences):
    Graph = nx.from_numpy_array(X,create_using=nx.MultiGraph())
    pg = sorted(nx.pagerank(Graph).items(),key= lambda x : x[1],reverse=True)
    sent = sorted([i[0] for i in pg[:15]])
    output = [sentences[i] for i in sent]
    return output



