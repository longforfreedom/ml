#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sklearn import linear_model
import numpy as np
##线性回归例子

x=np.arange(0,100).reshape(100,1)
y=(np.arange(0,100)*2+10).reshape(100,1)
x_test=np.arange(100,110).reshape(10,1)
#y = x*2 + 10
#模型训练
linear = linear_model.LinearRegression()
linear.fit(x,y)
linear.score(x,y)

print linear.coef_
print linear.intercept_

#测试
predicted= linear.predict(x_test)
print predicted
#预测结果


#print x
#print y

###多个维度
#x = np.array( [ [i,i] for i in  xrange(0,100)]).reshape(100,2)
#y = np.array(   [ [i,i*2+10] for i in xrange(0,100)] ).reshape(100,2)
