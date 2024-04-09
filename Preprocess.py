import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download("stopwords")
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def Preprocess(Filename):
    with open(Filename) as f:
        data = f.readlines()[10:]
        data = data[:-13]
        # Sentence Splitting
        sentences = []
        for i in data:
            sentences += nltk.sent_tokenize(i)
        # Word Splitting
        words_in_sentence = []
        for i in sentences:
            words_in_sentence.append(nltk.word_tokenize(i))
        Stop_word = stopwords.words('english')
        words_nostop_in_sentence = []
        for i in words_in_sentence:
            temp = [word for word in i if word not in Stop_word and word.isalnum()==True]
            words_nostop_in_sentence.append(temp)
        root_per_sentence = []
        obj = nltk.WordNetLemmatizer()

        for i in words_nostop_in_sentence:
            temp  = [obj.lemmatize(j) for j in i ] 
            root_per_sentence.append(temp)
    return sentences,root_per_sentence,words_in_sentence
