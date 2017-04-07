#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit ([[0, 0],[1,1.5], [1, 1], [2, 2], [3, 3]], [2,1,4,6,8])
##预测[5,5]的值
print reg.predict([[4,4],[5,5],[4,5]])
##打印系统数
print reg.coef_
print reg.intercept_
