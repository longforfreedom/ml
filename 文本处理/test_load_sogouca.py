#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from load_sogou_news import *
class TestLoadSougouCa(unittest.TestCase):
    def test_download(self):
        download_file(sogouca_sample_metadata,"./xx.dat")
        self.assertTrue(os.path.exists("./xx.dat"))
    
    def  test_load(self):
        for i in load_sogou_news(data_home="data",is_ca=False):
            print("{1}".format(*i))
        self.assertEqual(1,1)