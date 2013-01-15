# -*- coding: utf-8 -*-
'''
Created on 09/01/2013

@author: Maria
'''

def Zero():
    nummer = 0
    myfile = open("Datalog1.txt", "w")
    myfile.write("Time/ms\tInput/Volts\n")
    for x in range (1,1002):
        
        myfile.write(str(nummer) + "\t0\n")
        nummer += 1
    
    myfile.close()
    
Zero()