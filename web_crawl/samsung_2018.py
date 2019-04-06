from konlpy.tag import Okt
import re  #정규표현식
# 한번 실행하고 삭제하거나 주석처리..계속 실행때마다 다운로드하면 느려짐
# ----------------------------------------------------------------------
#한국어사전
# import nltk
# nltk.download()
# ----------------------------------------------------------------------
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt

okt = Okt()
ctx = 'C:/Users/ezen/PycharmProjects/test2/data/'
filename = ctx + 'kr-Report_2018.txt'

with open(filename, 'r', encoding='utf-8') as f:
    texts = f.read()

texts = texts.replace('\n', '')
tokenizer = re.compile('[^ ㄱ-힣]+')
texts = tokenizer.sub('', texts)

tokens = word_tokenize(texts)

# print(texts[:10])

noun_token =[]
for token in tokens:
    token_pos = okt.pos(token)
    temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']
    if len(''.join(temp)) > 1:
        noun_token.append(''.join(temp))
texts = ' '.join(noun_token)
# print(texts[:300])

with open(ctx+'stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords = f.read()

stopwords = stopwords.split(' ')
# print(stopwords[:10])

texts = [text for text in tokens if text not in stopwords]
freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)
# print(freqtxt[:30])

okt.pos('가치창출')
okt.pos('갤러시') # 오타는 갤럭시로 처리

wcloud = WordCloud(ctx+'D2Coding.ttf', relative_scaling=0.2,
                   background_color='white').generate(' '.join(texts))

plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

























