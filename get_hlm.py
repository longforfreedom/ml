#!/usr/bin/env python
# -*- coding:utf-8 -*-
############################################
# 从网易阅读抓取红楼梦
# pip install splinter
# 下载chromedriver放在chrome的安装目录下面
############################################

import time
import random
import codecs
from splinter import Browser
from selenium.webdriver.common.keys import Keys

executable_path = {
    'executable_path': 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
}

browser = Browser('chrome', **executable_path)
browser.visit(
    'http://yuedu.163.com/book_reader/422fa33a-c407-4e82-81f5-b973ab3585fc_4')


sections = []
datafile = codecs.open("E:/workspace/ml/data/hlm.txt",'w','utf-8')
#datafile = open("E:/workspace/ml/data/hlm.txt",'w',encoding='utf-8')
def get_new_content():
    """解析内容"""
    for words in browser.find_by_xpath('//*[@id="J_Portrait"]/div/div[2]/div/div[2]/div[1]/h1') \
            + browser.find_by_xpath('//*[@id="J_Portrait"]/div/div[2]/div/div[2]/div[1]/p'):
        section = words.value.strip()

        if not section.isspace()   and section not in sections:
            sections.append(section)
            print("p:{}".format(section))
            datafile.write(section+"\n")
            datafile.flush()
        else:
            pass
            #print("{} is already exists or lenght is zero:".format(section))

if __name__ == '__main__':
    try:
        for i in range(1, 100000):
            print(i)
            browser.driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
            get_new_content()

            end_flag = browser.find_by_xpath('//*[@id="J_Portrait"]/div/div[2]/div/div/div[2]').value.strip()
            if end_flag is not None and len(end_flag) == "100%":
                break
            time.sleep(random.randint(0, 3))
    except Exception as inst:
        print(inst)

    finally:
        datafile.close()
        print("-" * 20)
        browser.quit()