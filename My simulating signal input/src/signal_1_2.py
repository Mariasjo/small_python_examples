# -*- coding: utf-8 -*-
'''
Created on 09/01/2013

@author: Maria
'''
import random

def Noise():
    nummer = 0
    tilfældig = 0
    myfile = open("Datalog2.txt", "w")
    myfile.write("Time/ms\tInput/Volts\n")
    for x in range (1,1002):
        tilf = random.uniform(-1,1)
        myfile.write(str(nummer) + "\t" + str("%.3f" % tilfældig) + "\n")
        nummer += 1
    myfile.close()

Noise()
    