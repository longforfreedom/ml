#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans

from sklearn import datasets
#iris = datasets.load_iris()

#X = np.array([[1, 2], [1, 4], [1, 0],[4, 2], [4, 4], [4, 0]])
##生成两组随机数据，指定范围，直观展现结果
X= np.vstack((np.random.random((100,2))+1,np.random.random((100,2))+3))
#plt.plot(X[:,0],X[:,1],'ro')
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
X_r = kmeans.labels_

for i,x in enumerate(X):
    plt.plot(x[0],x[1],'go' if X_r[i] == 1 else 'ro')
  
#展现聚集中心
X_c = kmeans.cluster_centers_
plt.plot(X_c[:,0],X_c[:,1],'yo')

#预测
X_p = np.array([ [4, 4],[0.5, 1],[3, 4],[2, 1]])
X_p_r = kmeans.predict(X_p)
r_plot = np.column_stack((X_p,X_p_r.reshape((4,1))))

#画出预测的点
[plt.plot(i[0],i[1],'ko' if i[2] == 1 else 'co') for i in r_plot]
#plt.plot(X_p[:,0],X_p[:,1],'go')


