#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
import numpy as np

if __name__=='__main__':
    data=[]
    with  open('pima-indians-diabetes.data') as dfile:
        data=np.array([[float(f) for f in  line.strip().split(',')] for line in dfile.readlines()])
    nb = GaussianNB()
    #nb = MultinomialNB()
    ## 前500行训练模型
    nb.fit(data[:500,:-1],data[:500,-1])
    
    ##剩余数据测试模型
    #print nb.predict(np.array([   3.    , 116.    ,   0.     ,  0.     ,  0.    ,  23.5 ,     0.187 ,  23.   ]).reshape(1,-1))
    p_r = nb.predict(data[500:,:-1])
    ## 实际结果
    r_r = data[500:,-1]  
    ## 预测正确个数
    right_num = np.count_nonzero(p_r == r_r)

    ## 正确率
    print  '正确率:%s' % (right_num*1.0/p_r.shape[0])

    print '--------------NaiveBayes-------iris------'
    from sklearn import datasets
    iris = datasets.load_iris()
    nb = GaussianNB()
    nb.fit(iris.data[:130],iris.target[:130])
    print  nb.predict(iris.data[130:])
    iris_r = nb.predict(iris.data[130:]) == iris.target[130:]
    right_num = np.count_nonzero(iris_r)
    print iris_r
    print '共预测样本:%d' %   iris.data[130:].shape[0]
    print '预测正确率:%f' %  (right_num*1.0/iris.data[130:].shape[0])


    print 'BernoulliNB --------------------------'
    from sklearn.naive_bayes import BernoulliNB
    X = np.random.randint(2, size=(6, 10))
    Y = np.array([1, 3, 3, 4, 4, 3])
    clf = BernoulliNB()
    clf.fit(X, Y)
    print(clf.predict(X[2:3]))


