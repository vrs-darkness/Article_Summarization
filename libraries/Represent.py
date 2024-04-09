import pandas as pd
import numpy as np
from gensim.models import FastText
def mag(vct):
    return np.sum(vct**2)
def ft_vector_similarity(v1,v2):
    return (np.dot(v1,v2.T) / ((mag(v1) * mag(v2))))[0][0]
def text_similarity(root_s1,root_s2,s1,s2):
    common_words = []
    
    for word in root_s1:
        if word in root_s2:
            common_words.append(word)
    similarity_score = len(common_words)/(np.log(len(s1)) + (np.log(len(s2))))
    return similarity_score
def Represent(root_per_sentence,words_in_sentence,sentences):
    fmodel = FastText(sentences=root_per_sentence,min_count=1,vector_size=150,window=5,workers=5,epochs=100)
    ft_vectors = [fmodel.wv[root_per_sentence[i]].sum(axis = 0).reshape(1,150) for i in range(len(root_per_sentence))]
    ### Representation 1 
    MAT1 = np.array([[ft_vector_similarity(ft_vectors[j],ft_vectors[i]) if i!=j else 0 for i in range(len(ft_vectors))] for j in range(len(ft_vectors))])
    ### Representation 2
    MAT2 = np.array([[text_similarity(root_per_sentence[i],root_per_sentence[j],words_in_sentence[i],words_in_sentence[j]) if i!=j else 0 for i in range(len(sentences))] for j in range(len(sentences))])
    ### Normalized Repesentation
    G = MAT1 + MAT2
    return G

