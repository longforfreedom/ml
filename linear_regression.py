#!/usr/bin/env python
# -*- coding:utf-8 -*-
#################################
#  线性回归实现
#  @author migle 2017-3-31
#
#
#################################
import numpy as np
class LinearRegression:
    def __init__(self):
        pass
    #正规方程(Normal Equation)算法实现    
    def train(self,X_n,Y):
        n_samples,n_features = X_n.shape
        #加一列:X0=1
        X=np.column_stack((np.ones(n_samples),X_n))
        self.theta = np.linalg.inv((X.T).dot(X)).dot(X.T).dot(Y)

    #梯度下降
    def train_gb(self,X_n,Y,theta,alpha,num_inters):
        n_samples,n_features = X_n.shape
        #加一列:X0=1
        X=np.column_stack((np.ones(n_samples),X_n))
        js = np.zeros((num_inters,1))
        self.theta = theta
        for i in xrange(num_inters):
            js[i] = self.cost_function(X,Y,self.theta)
            self.theta = self.theta - alpha/n_samples * (X.T).dot((X.dot(self.theta) -Y))
        return (self.theta,js)

    ##代价函数
    def cost_function(self,X,Y,theta):
        n_samples,n_features = X.shape
        #X is need M*(n+1)
        j =  np.sum((X.dot(theta) - Y)**2)/(2*n_samples)
        return j
  
    def predict(self,X_n):
        n_samples,n_features = X_n.shape
        #加一列:X0=1
        X=np.column_stack((np.ones(n_samples),X_n))
        return X.dot(self.theta) 

if __name__ =='__main__':
    ##正规方程测试
    #X.shape=M*(N+1)
    #Y.shape=M*1
    #theta.shape=(N+1)*1
    #X_n=np.arange(100).reshape(100,1)
     
    #lr = LinearRegression()
    #lr.train(X_n[:30],X_n[:30]*2)
    
    #print  lr.predict(X_n[30:,:])
    #print lr.theta.shape
 
   
    ##########梯度下降测试
    X_n=np.arange(100).reshape(100,1)
    Y= X_n[:30]*2
    lr = LinearRegression()
    #可以调整 alpha和num_inters的值,使两条直线基本重合,0.006,num_inters=1000
    detail = lr.train_gb(X_n[:30],X_n[:30]*2,np.array([[0],[1]]),0.001,1000)
    
    ## jupyter中运行非常方便
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10,10))
    plt.plot(X_n[:30],Y,'ro')
    plt.plot(X_n[:30],lr.predict(X_n[:30]))
    
    print detail


