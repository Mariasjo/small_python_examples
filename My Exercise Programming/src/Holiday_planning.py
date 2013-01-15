# -*- coding: utf-8 -*-
'''
Created on 28/11/2012

@author: Maria
'''

myFile = open("ferieplan2013 14.txt", encoding="utf-8")

myList = []

def skipTwoLine(myFile):
    myFile.readline()
    myFile.readline()  

skipTwoLine(myFile)

ferie = {}

def readdate():
    dateLine = myFile.readline()
    dateparts = dateLine.split('-')
    startdate = dateparts[0]
    if len(dateparts) == 2:
        enddate = dateparts[1]
        enddate = enddate.strip().strip(")(")
    else:
        enddate = startdate
    print(enddate)      
    return startdate, enddate

def FirstHoliday():
    while True:
        ferie = {}
        print(myList)
        ferie["description"] = myFile.readline().strip() 
        startdate, enddate = readdate()
        if startdate == '':
            break
        ferie["startdate"] = startdate.strip().strip(')(')
        ferie["enddate"] = enddate.strip().strip(')(')
        myList.append(ferie)
    return myList

#def 

#FirstHoliday()
#print(myList)
