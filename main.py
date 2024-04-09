from model import Model
from Preprocess import Preprocess
from Represent import Represent
from extract import Extract

# Extract(input("Enter the medium "))
sentences,root_per_sentence,words_in_sentence  = Preprocess("Text.txt")
Graph = Represent(root_per_sentence,words_in_sentence,sentences)
output = Model(Graph,sentences)



print("Summary : ")

for i in output:
    print(i)
