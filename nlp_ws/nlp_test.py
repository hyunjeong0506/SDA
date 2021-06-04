import pandas as pd
from pandas.core.frame import DataFrame
import konlpy
from konlpy.tag import Kkma, Okt
import nltk

excel_path = './data.xlsx'
dataframe = pd.read_excel(excel_path)
data = dataframe['개선사항']

sentence = data[79]
print("Test sentence : {}".format(sentence))

okt = Okt()
words = okt.pos(sentence)

# Define a chunk grammar, or chunking rules, then chunk
grammar = """
NP: {<N.*>*<Suffix>?}   # Noun phrase
VP: {<V.*>*}            # Verb phrase
AP: {<A.*>*}            # Adjective phrase
"""
parser = nltk.RegexpParser(grammar)
chunks = parser.parse(words)

print("# Print whole tree")
print(chunks.pprint())

NP = []
AP = []
VP = []
print("\n# Print noun phrases only")
for subtree in chunks.subtrees():
    if subtree.label() == 'NP':
        NP.append(list(subtree))
    if subtree.label() == 'AP':
        AP.append(list(subtree))
    if subtree.label() == 'VP':
        VP.append(list(subtree))
    #     print(' '.join((e[0] for e in list(subtree))))
    #     print(subtree.pprint())

print("=================================")
print(NP)
print(AP)
print(VP)
print("=================================")        

chunks.draw()

# result = okt.pos(sentence)

# noun = []
# adjective = []
# verb = []

# for token in result:
#     print(token[1])
#     if token[1] == 'Noun':
#         noun.append(token[0])
#     elif token[1] == 'Adjective':
#         adjective.append(token[0])
#     elif token[1] == 'Verb':
#         verb.append(token[0])


# print("=================================")
# print(noun)
# print(adjective)
# print(verb)
# print("=================================")


# 처음에는 명사 빈도수 계산

# 빈도가 높은 명사(구)에 대해 형용사구와 동사구를 확인

# word2vec을 사용하여 빈도가 높은 명사에 대한 다른 단어들을 확인