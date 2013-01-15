# -*- coding: utf-8 -*-
'''
Created on 01/11/2012

@author: Maria
'''


def do_plus(x, y):
    return(x + y)

print(do_plus(4,3))
print(do_plus("hej ","8"))

print("------------------ex 5.1 done----------------")  

def do_plus_better(x, y):
    if type(x) == type(2) and type(y) == type(2):
        return(x + y)
    if type(x) == type("") and type(y) == type(""):
        return(x + y) 
    else:
        raise TypeError
    
print(do_plus_better(2,3))
print(do_plus_better("2", "3"))
print(do_plus_better(2,"3"))
print(do_plus_better("2",3))

print("------------------ex 5.2 done----------------")  