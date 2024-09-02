from model import Model
from Preprocess import Preprocess
from Represent import Represent
from extract import Extract


def main(D):
    Extract(D)
    sentences,root_per_sentence,words_in_sentence  = Preprocess("Text.txt")
    Graph = Represent(root_per_sentence,words_in_sentence,sentences)
    output = Model(Graph,sentences)
    return output
