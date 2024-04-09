import networkx as nx
import numpy as np

def Model(X,sentences):
    Graph = nx.from_numpy_array(X,create_using=nx.MultiGraph())
    pg = sorted(nx.pagerank(Graph).items(),key= lambda x : x[1],reverse=True)
    lengt = int(len(sentences) * 0.2)
    sent = sorted([i[0] for i in pg[:lengt]])
    output = [sentences[i] for i in sent]
    return output



