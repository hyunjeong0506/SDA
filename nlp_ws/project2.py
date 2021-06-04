import pandas as pd
import konlpy
from konlpy.tag import Kkma, Okt
import nltk

excel_path = './data.xlsx'
dataframe = pd.read_excel(excel_path, engine='openpyxl' )
data = dataframe['개선사항']

test_sentence = data[2]
print("Test sentence : {}".format(test_sentence))

okt = Okt()
words = okt.pos(test_sentence)

# Define a chunk grammar, or chunking rules, then chunk
grammar = """
NP: {<N.*>*<Suffix>?}   # Noun phrase
VP: {<V.*>*}            # Verb phrase
AP: {<A.*>*}            # Adjective phrase
"""
parser = nltk.RegexpParser(grammar)

# # Test 시작 
# chunks = parser.parse(words)

# print("# Print whole tree")
# print(chunks.pprint())

# NPs = []
# APs = []
# VPs = []
# print("\n# Print noun phrases only")
# for subtree in chunks.subtrees():
#     if subtree.label() == 'NP':
#         NP = []
#         for e in list(subtree):
#             NP.append(e[0])
#         NPs.append(NP)
#     if subtree.label() == 'AP':
#         AP = []
#         for e in list(subtree):
#             AP.append(e[0])
#         APs.append(AP)
#     if subtree.label() == 'VP':
#         VP = []
#         for e in list(subtree):
#             VP.append(e[0])
#         VPs.append(VP)

#     #     print(' '.join((e[0] for e in list(subtree))))
#     #     print(subtree.pprint())

# print("=================================")
# print("NPs : {}".format(NPs))
# print("APs : {}".format(APs))
# print("VPs : {}".format(VPs))
# print("=================================")        

# chunks.draw()

# Test 끝

## Whole
whole_tokenized_sentence = []
# i = 1
for sentence in data:
    words = okt.pos(sentence)
    chunks = parser.parse(words)

    NPs = ["NP"]
    APs = ["AP"]
    VPs = ["VP"]
    for subtree in chunks.subtrees():
        if subtree.label() == 'NP':
            NP = []
            for e in list(subtree):
                NP.append(e[0])
            NPs.append(NP)
        if subtree.label() == 'AP':
            AP = []
            for e in list(subtree):
                AP.append(e[0])
            APs.append(AP)
        if subtree.label() == 'VP':
            VP = []
            for e in list(subtree):
                VP.append(e[0])
            VPs.append(VP)
    
    tokenized_sentence = [NPs, APs, VPs]
    whole_tokenized_sentence.append(tokenized_sentence)

    # i += 1
    # if i == 3:
    #     break

target_noun = '안내'

for sentence in whole_tokenized_sentence:
    # print(sentence)
    for NP in sentence[0]:
        if target_noun in NP:
            print("======================================")
            print(target_noun, "와 같이 있는 명사들과 해당하는 형용사구와 동사구는 다음과 같습니다.")
            print(sentence[0])
            print(sentence[1])
            print(sentence[2])
            print("======================================")

