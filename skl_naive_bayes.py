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
    ## 前300行训练模型
    nb.fit(data[:500,:-1],data[:500,-1])
    
    ##剩余数据测试模型
    #print nb.predict(np.array([   3.    , 116.    ,   0.     ,  0.     ,  0.    ,  23.5 ,     0.187 ,  23.   ]).reshape(1,-1))
    p_r = nb.predict(data[500:,:-1])
    ## 实际结果
    r_r = data[500:,-1]  
    ## 预测正确个数
    right_num = np.count_nonzero(p_r == r_r)

    ## 正确率
    print right_num*1.0/p_r.shape[0]


