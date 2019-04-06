from konlpy.tag import Okt
import re  #정규표현식
# 한번 실행하고 삭제하거나 주석처리..계속 실행때마다 다운로드하면 느려짐
# ----------------------------------------------------------------------
#한국어사전
# import nltk
# nltk.download()
# ----------------------------------------------------------------------
from nltk.tokenize import word_tokenize

ctx = 'C:/Users/ezen/PycharmProjects/test2/data/'
filename = ctx + 'kr-Report_2018.txt'

with open(filename, 'r', encoding='utf-8') as f:
    texts = f.read()

texts = texts.replace('\n', '')
tokenizer = re.compile('[^ ㄱ-힣]+')
texts = tokenizer.sub('', texts)

tokens = word_tokenize(texts)

print(texts[:10])
