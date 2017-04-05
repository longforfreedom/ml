#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import sys
###############################
#  朴素贝叶斯实现
#  @author migle 2017-3-31
#
###############################
class GaussianNB:
   #连续值，高斯分布模型
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
        #依次计算不同分类下的概率:
        for i,c_i in enumerate(self.classes):
            x_i = x[y==c_i,:] 
            #如果是连续值，要用正态分布密度分布函数,计算均值，标准差
            self.mean[i,:] = x_i.mean(axis=0)
            self.std[i,:] = x_i.std(axis=0)
            self.y_p[i] = np.float(x_i.shape[0]) / self.n_samples  
    def predict(self,x):
        rs =  np.zeros(x.shape[0])
        for j in range(x.shape[0]):
            r = np.zeros(self.classes.size)
            for i in range(self.classes.size):
                tmp = np.exp(-(x[j] - self.mean[i,:])**2/(self.std[i,:]**2*2))
                tmp1 = tmp/(self.std[i,:]* np.sqrt(2*np.pi))
                r[i] = np.multiply.reduce(tmp1)*self.y_p[i]
            rs[j] = self.classes[r.argmax()]
        return rs

class NaiveBayes:
    #离散值，标准贝叶斯公式
    def __init__(self):
        pass
    def train(self,x,y):
        self.n_samples,self.n_features = x.shape
        self.classes = np.unique(y)
        n_classes = self.classes.shape[0]
        self.y_p  = np.zeros(n_classes)
        #依次计算不同分类下的概率:
        #P(X|Y)
        self.y_x_p={}
        for i,c_i in enumerate(self.classes):
            x_i = x[y==c_i,:] 
            #计算P(Y)
            self.y_p[i] = np.float(x_i.shape[0]) / self.n_samples 
            self.y_x_p[c_i] = []
            for j in range(self.n_features):
                    self.y_x_p[c_i].append(self.__f_p(x_i[:,j]))

            print self.y_x_p
    def predict(self,x):
        rs =  np.zeros(x.shape[0])
        for j in range(x.shape[0]):
            r = np.zeros(self.classes.size)
            for i,c_i in enumerate(self.classes):
                r[i] = self.y_p[i]
                for f in range(self.n_features):
                    r[i] = r[i] * self.y_x_p[c_i][f][x[j,f]]  #if x[j,f] in self.y_x_p[c_i][f][x[j,f]]  else r[i]  #避免为0整体为0 
            print r
            print r.argmax()
            print self.classes
            rs[j] = self.classes[r.argmax()]
        return rs

    #计算P(X|Y)
    def __f_p(self,featuer):
        size = len(featuer)
        d={}
        for i in featuer:
            d[i] = 1 if i not in d else d[i]+1
        for k in d: 
            d[k] = d[k]*1.0/size
        return d
            
        
if __name__=='__main__':
    data=[]
    #with  open('pima-indians-diabetes.data') as dfile:
    #    data=np.array([[float(f) for f in  line.strip().split(',')] for line in dfile.readlines()])
#
    #print 'load data rows:%d cloumns:%d' % data.shape 
#
    #nbayes = GaussianNB()
    #nbayes.train(data[:500,:-1],data[:500,-1])
#
    ##nbayes.predict(np.array([float(f) for f in  sys.argv[1].strip().split(',')]))
    #p_r = nbayes.predict(data[500:,:-1])
    #r_r = data[500:,-1]
    ##print p_r == r_r
    #right_num = np.count_nonzero(p_r == r_r)
    #print '共预测样本:%d' %   p_r.shape[0]
    #print '预测正确率:%f' %  (right_num*1.0/p_r.shape[0])

    #print data[500:501,-1]

    #x=[v[0:-2] for v in data]
    #y=[[v[-1]]   for v in data]
    #print x[:10]
    #print y[:10]

    X = np.random.randint(2, size=(6, 10))
    Y = np.array([1, 3, 3, 4, 4, 3])

    from sklearn.naive_bayes import BernoulliNB
    clf = BernoulliNB()
    clf.fit(X, Y)
    print(clf.predict(X[2:3]))

    nb = NaiveBayes()
    nb.train(X, Y)
    print(nb.predict(X[2:3]))
