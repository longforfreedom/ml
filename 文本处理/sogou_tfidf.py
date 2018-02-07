#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scipy.sparse.csr.csr_matrix
from sklearn.feature_extraction.text import CountVectorizer
import jieba 
from load_sogouca import load_sogouca
sentences = [" ".join(filter(lambda s:s.isalnum,jieba.lcut(i[3]))) for i in load_sogouca(data_home="./data/")]

print(len(sentences))
count_vect = CountVectorizer()
count_vect.fit(sentences)
#x =  count_vect.fit_transform(sentences)
print(dir(count_vect))
#print(x[0])