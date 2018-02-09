#!/usr/bin/env python
# -*- coding:utf-8 -*-

from time import time
import multiprocessing
import  gensim 
#from gensim.models.word2vec import LineSentence
import jieba
from load_sogou_news import load_sogou_news
from os.path import join as path_join
from os.path import exists as path_exists
if __name__ == '__main__':
    start  = time()
    sentences = [jieba.lcut(i[3]) for i in load_sogou_news(data_home="./data/")]
    print(len(sentences))
    model = gensim.models.Word2Vec(sentences,
                                   size=200,
                                   window=10,
                                   min_count=10,
                                   workers=multiprocessing.cpu_count())
    model.save("data/word2vec_gensim")
    model.wv.save_word2vec_format("data/model/word2vec_org",
                                  "data/model/vocabulary",
                                  binary=False)
    print("total times: %d seconds" % (time()-start))
    