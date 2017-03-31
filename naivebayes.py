#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import sys

class NaiveBayes:
    def __init__(self):
        pass
    def train(self,x,y):
        self.n_samples,self.n_features = x.shape
        #共几种分类
        self.classes = np.unique(y)
        n_classes = np.unique(y).shape[0]
        self.mean = np.zeros((n_classes, self.n_features))
        self.std  = np.zeros((n_classes, self.n_features))
        self.y_p  = np.zeros(n_classes)

        #print 'P(A):%f' % p_y_1 

        for i,c_i in enumerate(self.classes):
            x_i = x[y==c_i,:] 
            self.mean[i,:] = x_i.mean(axis=0)
            self.std[i,:] = x_i.std(axis=0)
            self.y_p[i] = np.float(x_i.shape[0]) / self.n_samples  #每一种分类的概率
            #如果是连续值，要用正态分布

    def predict(self,x):
        print '*'*20
        print x
        r = np.zeros(self.classes.size)
        print self.classes

        for i in range(self.classes.size):
            tmp = np.exp(-(x - self.mean[i,:])**2/(self.std[i,:]**2*2))
            tmp1 = tmp/(self.std[i,:]* np.sqrt(2*np.pi))
            print '-'*10
            print i
            print tmp1
            r[i] = np.multiply.reduce(tmp1)
        print '+'*20
        print r
        print self.classes[r.argmax()]

if __name__=='__main__':
    data=[]
    with  open('pima-indians-diabetes.data') as dfile:
        data=np.array([[float(f) for f in  line.strip().split(',')] for line in dfile.readlines()])

    print 'load data rows:%d cloumns:%d' % data.shape 

    nbayes = NaiveBayes()
    nbayes.train(data[:300,:-1],data[:300,-1])

    #nbayes.predict(np.array([float(f) for f in  sys.argv[1].strip().split(',')]))
    nbayes.predict(data[500:501,:-1][0])
    print data[500:501,-1]

    #x=[v[0:-2] for v in data]
    #y=[[v[-1]]   for v in data]
    #print x[:10]
    #print y[:10]
