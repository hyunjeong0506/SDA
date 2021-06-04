import pandas as pd
import matplotlib.pyplot as plt
import konlpy
from konlpy.tag import Kkma, Okt
from gensim.models import Word2Vec

excel_path = './data.xlsx'
dataframe = pd.read_excel(excel_path, engine='openpyxl')
data = dataframe['개선사항']

test_sentence = data[2]
print("Test sentence : {}".format(test_sentence))

# 정규 표현식을 통한 한글 외 문자 제거
dataframe['개선사항'] = dataframe['개선사항'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")

# print(dataframe[:5])

# 불용어 정의
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

# 형태소 분석기 OKT를 사용한 토큰화 작업 (다소 시간 소요)
okt = Okt()
tokenized_data = []
for sentence in dataframe['개선사항']:
    temp_X = okt.morphs(sentence, stem=True) # 토큰화
    temp_X = [word for word in temp_X if not word in stopwords] # 불용어 제거
    tokenized_data.append(temp_X)

# 답변 길이 분포 확인
print('답변의 최대 길이 :',max(len(l) for l in tokenized_data))
print('답변의 평균 길이 :',sum(map(len, tokenized_data))/len(tokenized_data))
plt.hist([len(s) for s in tokenized_data], bins=50)
plt.xlabel('length of samples')
plt.ylabel('number of samples')
# plt.show()

model = Word2Vec(sentences = tokenized_data, vector_size = 100, window = 5, min_count = 5, workers = 4, sg = 0)

print(model.wv.most_similar("안내"))