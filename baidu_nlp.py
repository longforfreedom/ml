#!/usr/bin/env python
#-*- coding:utf-8 -*-

from aip import AipNlp

APP_ID='9369538' 
API_KEY='ubtTob21IlHwtZ3CUmMSfaAg' 
SECRET_KEY='H3Im2tQ1gFOm2S5ksbxQReiPIYYlOFYK' 

aipNlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)

#result = aipNlp.commentTag('特斯拉外观很漂亮')
#print result

r =aipNlp.dnnlm("床前明月光，疑是地上霜")
print r['result']['seq_prob']
for w in  r['result']['seq_seg']:
    print w
