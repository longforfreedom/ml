#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import string
import sys
from PIL import Image,ImageDraw,ImageFont,ImageFilter


#字体的位置，不同版本的系统会有不同
font_path = './fonts/simsun.ttc'
#生成几位数的验证码
number = 1
#生成验证码图片的高度和宽度
size = (20,20)
#背景颜色，默认为白色
bgcolor = (255,255,255)
#字体颜色，默认为蓝色
fontcolor = (0,0,255)
#干扰线颜色。默认为红色
linecolor = (255,0,0)
#是否要加入干扰线
draw_line = True
#加入干扰线条数的上下限
line_number = (1,5)
 
#用来随机生成一个字符串
def gene_text():
    #source = list(string.ascii_letters)
    source = list(string.digits)
    for index in range(0,10):
        source.append(str(index))
    return ''.join(random.sample(source,number))#number是生成验证码的位数
#用来绘制干扰线
def gene_line(draw,width,height):
    begin = (random.randint(0, width), random.randint(0, height))
    end = (random.randint(0, width), random.randint(0, height))
    draw.line([begin, end], fill = linecolor)
 
#生成验证码
def gene_captcha(filename,code):
    width,height = size #宽和高
    image = Image.new('RGB',(width,height),bgcolor) #创建图片
    font = ImageFont.truetype(font_path,25) #验证码的字体
    draw = ImageDraw.Draw(image)  #创建画笔
    #text = gene_text() #生成字符串
    font_width, font_height = font.getsize(code)
    draw.text(((width - font_width) / number, (height - font_height) / number),code,
            font= font,fill=fontcolor) #填充字符串
    if draw_line:
        gene_line(draw,width,height)
    # image = image.transform((width+30,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
    image = image.transform((width+20,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE) #滤镜，边界加强
    image.save(filename) #保存验证码图片

if __name__ == "__main__":
    
    train_num = 600
    test_num = 100
    print("需要生成:%d 个图片" % (test_num+train_num))

    train_label = open("train_label.txt",'w')
    test_label = open("test_label.txt",'w')

    for i in range(1,train_num+1):
        print("生成第%d个训练" % i)
        code = gene_text()
        fpath =  "train/" + str(i) +".jpg"
        gene_captcha(fpath,code)
        train_label.write("%s\t%s\n" % (fpath,code))

    for i in range(1,test_num+1):
        print("生成第%d个测试" % i)
        code = gene_text()
        fpath =  "test/" + str(i) +".jpg"
        gene_captcha(fpath,code)
        test_label.write("%s\t%s\n" % (fpath,code))

    train_label.close()
    test_label.close()