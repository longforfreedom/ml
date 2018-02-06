#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from load_sogouca import *
class TestLoadSougouCa(unittest.TestCase):
    def test_download(self):
        download_file(sogouca_sample_metadata,"./xx.dat")
        self.assertTrue(os.path.exists("./xx.dat"))