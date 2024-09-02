import requests
from bs4 import BeautifulSoup
import numpy as np
import nltk
from nltk.corpus import stopwords
from gensim.models import FastText


class Summarize:
    def __init__(self):
        pass

    def Extract(self, URL: str):
        pages = requests.get(URL)
        soup = BeautifulSoup(pages.text, "lxml")
        data = []
        for i in soup.find_all("p"):
            data.append(i.text)
        information = ""
        for i in data:
            information += (i + "\n")
        self.data = information

    def Preprocess(self):
        data = self.data.split("\n")
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
            temp = [word for word in i if (word not in Stop_word and
                    word.isalnum())]
            words_nostop_in_sentence.append(temp)
        root_per_sentence = []
        obj = nltk.WordNetLemmatizer()

        for i in words_nostop_in_sentence:
            temp = [obj.lemmatize(j) for j in i]
            root_per_sentence.append(temp)
        q = 0
        while (q < len(root_per_sentence)):
            if (len(root_per_sentence[q]) < 2):
                root_per_sentence.pop(q)
                sentences.pop(q)
                words_in_sentence.pop(q)
            else:
                q += 1
        return sentences, root_per_sentence, words_in_sentence

    def _mag(self, vct):
        return np.sum(vct**2)

    def _ft_vector_similarity(self, v1, v2):
        return (np.dot(v1, v2.T) / ((self._mag(v1) * self._mag(v2))))[0][0]

    def _text_similarity(self, root_s1, root_s2, s1, s2):
        common_words = []
        for word in root_s1:
            if word in root_s2:
                common_words.append(word)
        similarity_score = len(common_words)/(np.log(len(s1)) + (
            np.log(len(s2))))
        return similarity_score

    def Represent(self, root_per_sentence, words_in_sentence, sentences):
        fmodel = FastText(sentences=root_per_sentence,
                          min_count=1,
                          vector_size=150,
                          window=5,
                          workers=5,
                          epochs=100)
        ft_vectors = [fmodel.wv[root_per_sentence[i]].sum(
            axis=0).reshape(1, 150) for i in range(len(root_per_sentence))]
        # Representation 1
        MAT1 = np.array([[self._ft_vector_similarity(ft_vectors[j],
                                                     ft_vectors[i]) if (
                                                         i != j) else 0 for i in range(
                                                             len(ft_vectors))] for j in range(len(ft_vectors))])
        # Representation 2
        MAT2 = np.array([[self._text_similarity(root_per_sentence[i],
                                                root_per_sentence[j],
                                                words_in_sentence[i],
                                                words_in_sentence[j]) if (i != j) else 0 for i in range(len(sentences))] for j in range(len(sentences))])
        # Normalized Repesentation
        G = MAT1 + MAT2
        return G

    def PageRank(self, G, d, Prob):
        Page_Rank = [Prob for i in range(G.shape[0])]
        for i in range(0, G.shape[0]):
            Page_Rank[i] = ((1 - d)/(G.shape[0])) + d * sum(
                [Page_Rank[i]/(j) for j in G[i]])
        return {idx: Page_Rank[idx] for idx in range(G.shape[0])}

    def Model(self, X, sentences):
        pg = self.PageRank(X, d=0.85, Prob=0.5).items()
        pg = sorted(pg, key=lambda x: x[1], reverse=True)
        lengt = int(len(sentences) * 0.2)
        sent = [pg[i][0] for i in range(lengt)]
        output = [sentences[i] for i in sent]
        return output

    async def Summarize_url(self, url):
        self.Extract(url)
        sentences, root_per_sentence, words_in_sentence = self.Preprocess()
        Graph = self.Represent(root_per_sentence, words_in_sentence, sentences)
        output = self.Model(Graph, sentences)
        result = ""
        for i in output:
            result += (i + "\n")
        return result

    async def Summarize_para(self, data):
        self.data = data
        sentences, root_per_sentence, words_in_sentence = self.Preprocess()
        Graph = self.Represent(root_per_sentence, words_in_sentence, sentences)
        output = self.Model(Graph, sentences)
        result = ""
        for i in output:
            result += (i + "\n")
        return result


# Test = Summarize()

# print(Test.Summarize_url(url="https://blog.medium.com/weve-added-77-countries-to-the-medium-partner-program-827a574fcdf0"))
