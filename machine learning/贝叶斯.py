import os
import time
import numpy as np
import pandas as pd
import jieba
from jieba import analyse
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer #词集转换成向量
from sklearn.naive_bayes import MultinomialNB #朴素贝叶斯多分类
from sklearn.metrics import classification_report
import gensim #自然语言处理库
from gensim import corpora,models,similarities

#data = np.loadtxt(r"D:\thu_news.tar\thu_news\thu_news\train.txt",encoding='utf-8')
#a = pd.DataFrame(data)
#a.to_csv(r'D:\Users\lijun\PycharmProjects\machine learning\1.csv',index=False,encoding='utf-8')


