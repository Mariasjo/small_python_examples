'''
Created on 21/11/2012

@author: Maria
'''
import unittest

import wuhuu


class Test(unittest.TestCase):


    def test_wuhuu(self):
        self.assertEqual("40", wuhuu.add("20", "20"), "fail")
        print(wuhuu.add("20", "20"))
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test.wuhuu']
    unittest.main()