# -*- coding: utf-8 -*-
'''
Created on 12/11/2012

@author: Maria
'''

lookFor = "milk"
lookIn = ["butter", "milk", "cheese"]

if lookFor == lookIn[0]:
    print("found it")
elif lookFor == lookIn[1]:
    print("found it ...")
else:
    print("did not find it")
    
    
if lookFor in lookIn:
    print(" its there ")
else: 
    print("its not there")
This is the best way to do it




List = ["cheese", "brie"]
if "milk" in List:
    print("Yes there is milk") 
elif "cake" in List:
    print("no there is cake")
else:
    print('nothing is there!')
    