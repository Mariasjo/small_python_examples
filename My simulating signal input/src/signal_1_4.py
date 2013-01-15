# -*- coding: utf-8 -*-
'''
Created on 10/01/2013

@author: Maria
'''
import math

def sine():
    nummer = 0
    sine = 0
    newsine = 0
    myfile = open("Datalog4.txt", "w")
    myfile.write("Time/ms\tInput/Volts\n")
    for x in range (1,51):       
        for x in range (1,21):
            myfile.write(str(nummer) + "\t" + str("%.3f" % sine) + "\n")
            nummer += 1
            newsine += 1
            sines = 2 * math.pi * newsine / 20
            sine = math.sin(sines)      
    myfile.close()   

sine()
