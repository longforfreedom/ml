#!/usr/bin/env python
# -*- coding:utf-8 -*-
#关键字分词
import jieba

with open('./data/keywords.txt','r') as f:
    for line in f:
        seg_list = jieba.cut(line)
        print '/ '.join(seg_list)

