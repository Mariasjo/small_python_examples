# -*- coding: utf-8 -*-
'''
Created on 12/11/2012

@author: Maria
'''
fridge = {"egg": "6 egg", "milk": "Thise minimilk", "cheese": "Emmentaler"}
food_sought = "cheese"

for foodKey in fridge:
    print("\nlooking at : %s", foodKey)
    if foodKey == food_sought:
        print("key: %s \tValue: %s"%(foodKey, fridge[food_sought] ))
        break
    
else:
    print("it is not here")
    
print("------------------ex 4.4 done----------------")    

fridge_list = []
for foodKey in fridge:
    fridge_list.append(foodKey)
print( fridge_list )

while fridge_list:
    if fridge_list.pop()==food_sought :
        print( "found it again ")
        break
else:
    print("not found")
    
print("--------------- ex 4.5 done--------------------------")

try:
    wrongKey = fridge["Beer"]
except KeyError:
    print( "we are out of beer")
    
try:
    goodKey = fridge["milk"]
except ''

print("--------------- ex 4.6 done--------------------------"