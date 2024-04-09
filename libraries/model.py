
import numpy as np

def PageRank(G,d,Prob):
    Page_Rank = [Prob for i in range(G.shape[0])]
    for i in range(0,G.shape[0]):
        Page_Rank[i] = ((1 -d)/G.shape[0]) +  d  * sum([Page_Rank[i]/j for j in G[i]])
    return {idx : Page_Rank[idx] for idx in range(G.shape[0]) }
def Model(X,sentences):
    pg = PageRank(X,d=0.85,Prob=0.5).items()
    pg = sorted(pg,key=lambda x : x[1] ,reverse=True)
    lengt = int(len(sentences) * 0.2)
    sent = [pg[i][0] for i in range(lengt)]
    output = [sentences[i] for i in sent]
    return output


