import pandas as pd
import konlpy
from konlpy.tag import Kkma, Okt
from collections import Counter
from wordcloud import WordCloud

excel_path = './data.xlsx'
dataframe = pd.read_excel(excel_path, engine='openpyxl')

data = dataframe['개선사항']

all_nouns = []

for sentence in data:
    okt = Okt()
    nouns = okt.nouns(sentence)
    for noun in nouns:
        if len(str(noun)) > 1:
            all_nouns.append(str(noun))

count = Counter(all_nouns)

# 명사 빈도 카운드
noun_freq = count.most_common(100)
for freq in noun_freq:
    print(freq)

font_path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'

word_cloud = WordCloud(font_path=font_path, background_color="white")
cloud = word_cloud.generate_from_frequencies(dict(noun_freq))

cloud.to_file('test.jpg')

# sentence = data[79]
# print("Test sentence : {}".format(sentence))

# count = Counter()