# -*- coding: utf-8 -*-
'''
Created on 08/01/2013

@author: Maria
'''

#def Makefile(file):
#    temp_path = 'C:\Users\Maria\workspace\My stimulating ex\src' + file
#    file = open(temp_path, 'w')
#    file.write('')
#    file.close()
#    print ('Exercution complete')
   
 
import random
import math

#signal_types = (ZERO, NOISE, SINUS) = (0,1,2)
def Zero():
    

t_start = 0.0
t_end = 1.0
t_step = 0.001

def tick():
    t_now = t_start
    while t_now < t_end:
        t_now = t_now + t_step
        yield t_now
 
    