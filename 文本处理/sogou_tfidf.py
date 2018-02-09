#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
import jieba
from load_sogou_news import load_sogou_news
sentences = [" ".join(filter(lambda s:s.isalnum, jieba.lcut(i[3])))
             for i in load_sogou_news(data_home="./data/", is_ca=False)]

print(len(sentences))
count_vect = CountVectorizer()
count_vect.fit(sentences)
#x =  count_vect.fit_transform(sentences)
print(dir(count_vect))
# print(x[0])
