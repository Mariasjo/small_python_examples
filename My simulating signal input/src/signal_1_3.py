# -*- coding: utf-8 -*-
'''
Created on 09/01/2013

@author: Maria
'''
import random


def Square():
    nummer = 0
    myfile = open("Datalog3.txt", "w")
    myfile.write("Time/ms\tInput/Volts\n")
    for x in range (1,1002):
        for x in range (1,6):
            myfile.write(str(nummer) + "\t1\n")
            nummer += 1
        for x in range (1,6):
            myfile.write(str(nummer) + "\t-1\n")
            nummer += 1
    
    myfile.close()
    
Square()