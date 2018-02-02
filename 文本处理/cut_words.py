#!/usr/bin/env python
# -*- coding:utf-8 -*-

import jieba

with open("./data/hlm-all.txt",encoding="utf-8") as data:
    for lines in data:
        seg_list = jieba.lcut(lines)
        print(seg_list)
