#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
class LinearRegression:
    def __init__(self):
        pass
    def train(self,X_n,Y):
        n_samples,n_features = X_n.shape
        print X_n.shape
        X=np.column_stack((np.ones(n_samples),X_n))
        print X
        self.theta = np.linalg.inv((X.T).dot(X)).dot(X.T).dot(Y)
        print self.theta
        
    def predict(self,X_n):
        n_samples,n_features = X_n.shape
        X=np.column_stack((np.ones(n_samples),X_n))
        return X.dot(self.theta) 

if __name__ =='__main__':
    X_n=np.arange(100).reshape(100,1)
     
    lr = LinearRegression()
    lr.train(X_n[:30],X_n[:30]*2)
    
    print  lr.predict(X_n[30:,:])


