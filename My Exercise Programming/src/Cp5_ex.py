# -*- coding: utf-8 -*-
'''
Created on 01/11/2012

@author: Maria
'''
import unittest

import ex_bina

class Test(unittest.TestCase):


    def test_bina(self):
        self.assertEqual("13", ex_bina.add("5", "8"), "Fail")
        
#    def test_bina(self):
#        self.assertEqual("11011", ex_bina.add("0110", "10101"), "Fail") It works!