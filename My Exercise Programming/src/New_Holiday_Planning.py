# -*- coding: utf-8 -*-
'''
Created on 30/11/2012

@author: Maria
'''
myFile = open("Ferieplan.txt", encoding="utf-8")    

keeprunning = []
    
mylist = []

def skiptwo(myFile):
    myFile.readline()
    myFile.readline()

skiptwo(myFile)

ferie = {}

def readdate():
    datolinie = myFile.readline()
    
    datoparts = datolinie.split(' - ')
    
    sd = datoparts[0]
    
    if len(datoparts) == 2:
        ed = datoparts[1]
    else:
        ed = sd
    return sd,ed
        
        
def Firstferie():
    while True: 
        ferie = {}
        
        ferie["ferietype"] = myFile.readline().strip().strip('/')
        for thiskey2 in ferie:
            if "Ferieplan" in ferie[thiskey2]:
                return Firstferie()
                
            else:
                break
        for thiskey3 in ferie:
            if "Kr. Himmelfartsferie" in ferie[thiskey3]:
                kristipart = ferie["ferietype"]
                kristiparts = kristipart.split(' - ')
                kristipartss = kristiparts[0]
                ed1 = kristiparts[1]
                kristi = kristipartss.split(' torsdag ')
                ft = kristi[0]
                sd1 = kristi[1]
                ferie["ferietype"] = ft
                ferie["startdate"] = "torsdag " + sd1
                ferie["enddate"] = ed1
                mylist.append(ferie)
                return Firstferie()
                
            else:
                break
        for thiskey in ferie:
            if "Undervisningsministeriets" in ferie[thiskey]:
                keeprunning.append("1")
                break 
            else:
                break
        sd,ed = readdate()
        ferie["startdate"] = sd.strip().strip(')(')
        ferie["enddate"] = ed.strip().strip(')(')
        if len(keeprunning) == 1:
            break
  
        
        mylist.append(ferie)

Firstferie()

print(mylist)