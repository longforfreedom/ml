#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from os.path import join as path_join
from os.path import exists as path_exists
import logging
from zipfile import ZipFile
from collections import namedtuple 
from collections import Counter  
import jieba
import jieba.analyse
"""加载数据，分词，TD-IDF,word2vec"""
logger = logging.getLogger(__name__)

logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s [line:%(lineno)d] %(levelname)s %(threadName)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S')

RemoteFileMetadata = namedtuple('RemoteFileMetadata',
                                ['filename', 'url', 'checksum'])

sogouca_sample_metadata = RemoteFileMetadata(
    filename='news_tensite_xml.smarty.zip',
    url='http://download.labs.sogou.com/dl/sogoulabdown/SogouCA/news_tensite_xml.smarty.zip',
    checksum='')

#全量数据需要验证 
# wget http://www.sogou.com/labs/sogoudownload/SogouCS/news_sohusite_xml.full.zip --http-user=longforfreedom@sogou.com --http-passwd=oNML0!kRwhpz5y89
sogouca_full_metadata = RemoteFileMetadata(
    filename='news_tensite_xml.full.zip',
    url='http://www.sogou.com/labs/resource/ftp.php?dir=/Data/SogouCA/news_tensite_xml.full.zip',
    checksum='')
sogoucs_sample_metadata = RemoteFileMetadata(
    filename='news_sohusite_xml.smarty.zip',
    url='http://download.labs.sogou.com/dl/sogoulabdown/SogouCS/news_sohusite_xml.smarty.zip',
    checksum='')

sogoucs_full_metadata = RemoteFileMetadata(
    filename='news_tensite_xml.full.zip',
    url='http://www.sogou.com/labs/resource/ftp.php?dir=/Data/SogouCA/news_tensite_xml.full.zip',
    checksum='')

def toutf8(line):
    """编码转成utf-8"""
    return line.decode('gbk', 'ignore').encode('utf-8').decode('utf-8', 'ignore')

def del_tag(line, tag_name):
    """删除xml标记"""
    start = 2 + len(tag_name)
    end = -3 - len(tag_name)
    return line[start:end]

def download_file(remote,filepath):
    """下载数据文件"""
    from  urllib import request
    request.urlretrieve(remote.url,filepath)
    #sogou没有提供checksum!就不做校验了
    return filepath

def load_sogou_news(data_home,is_ca=True,is_sample = True, download_if_missing=True):
    """
    [全网新闻数据(SogouCA)](http://www.sogou.com/labs/resource/ca.php)  
    [搜狐新闻数据(SogouCS)](http://www.sogou.com/labs/resource/cs.php)
    不是标准的XML格式，特殊字符没有转义 

    is_ca=True加载全网新闻数据

    """
    if is_ca:
        metadata = sogouca_sample_metadata if is_sample else sogouca_full_metadata
    else:
        metadata = sogoucs_sample_metadata if is_sample else sogoucs_full_metadata

    if not path_exists(data_home):
        os.makedirs(data_home)

    file_path = path_join(data_home,metadata.filename)
    if not path_exists(file_path):
        if download_if_missing:
            logger.info('download sougou news...')
            download_file(metadata,file_path)                            
        else:
            raise IOError('sogounews data not found! [%s]' % file_path)
        
    def format_line(line, tag):
        """简便封装"""
        return del_tag(toutf8(line.strip()), tag)

    with ZipFile(file_path) as zip_xml:
        logger.debug('read data from zip file %s ',file_path)
        for xml in zip_xml.namelist():
            with zip_xml.open(xml) as xml:
                for lines in xml:
                    if lines.strip() == b'<doc>':
                        logger.debug('start')
                        url = format_line(xml.readline(), 'url')
                        docno = format_line(xml.readline(), 'docno')
                        contenttitle = format_line(
                            xml.readline(), 'contenttitle')
                        content = format_line(xml.readline(), 'content')
                        if xml.readline().strip() == b'</doc>':
                            logger.debug('end:%s',docno)
                        yield (docno, url, contenttitle, content)


if __name__ == '__main__':
    wp_path = path_join(os.path.dirname(__file__),'data-test')
    file = open(path_join(wp_path,'x.txt'), 'w', encoding='utf-8')
    words_count={}
    for i in load_sogou_news(data_home=wp_path):
        file.write('{}\n'.format(i[1]))
        #抽取关键字
        #tag1 = jieba.analyse.extract_tags(i[3],topK=10)
        #tag2 = jieba.analyse.textrank(i[3],topK=10)
        #print("{} : {}".format(i[2],",".join(tag1)))
        #print("{} : {}".format(i[2],",".join(tag2)))
        #print("-"*20)
        #分词
        seg_list = jieba.lcut(i[3])
        for seg in  seg_list:
            if seg not in words_count:
                #if seg in '，。、“ .）\（；＃！》《\,': #['，','。','、','“',' ','.','）','\,','（','；','＃','！','》','《']:
                #    continue
                if not seg.isalnum():
                    continue
                words_count[seg] = 1
                #print(seg)
            else:
                words_count[seg] = words_count[seg] + 1

    print(len(words_count))
    c = Counter(words_count)
    for k in c.most_common(100):
        print('{0}:{1}'.format(*k))