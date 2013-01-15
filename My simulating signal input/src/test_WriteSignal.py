'''
Created on 10/01/2013

@author: Maria
'''
import unittest
import filecmp
import filename''

class Test(unittest.TestCase):


    def testName(self):
        dklsg.write_to_file()
        
        result = filecmp.cmp("testing.dat", "", shallow=false)
        
        self.assertTrue(result, "Output file is wrong")

        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()