#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

categories = ['alt.atheism', 'soc.religion.christian',
              'comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(data_home="./data",
    subset='train', categories=categories, shuffle=True, random_state=42)
#print(dir(twenty_train))
#['DESCR', 'data', 'description', 'filenames', 'target', 'target_names']
#print(twenty_train.data[0])
#print(twenty_train.target[0])
#print(twenty_train.target_names[0])

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print(type(X_train_counts))
print(X_train_counts.shape)
print(len(twenty_train.data))
print(count_vect.vocabulary_.get('algorithm'))
print(count_vect.vocabulary_.get('mail'))
print('-'*20)

import sklearn.feature_extraction.DictVectorizer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

#print(X_train_tfidf.shape)
#print(X_train_counts[1])
print(X_train_counts.shape)
print('-'*20)
print(X_train_tfidf[0])
print('-'*20)
print(X_train_tfidf.shape)

#print(dir(count_vect))
#clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
