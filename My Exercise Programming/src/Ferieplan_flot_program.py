# -*- coding: utf-8 -*-
'''
Created on 30/11/2012

@author: Maria
'''
myFile = open("Ferieplan.txt", encoding="utf-8")  
keeprunning = []   
myvacationlist = []

def Vacationloop():
    while True: 
        vacation = {}
        
        vacation["vacationtype"] = myFile.readline().strip().strip('/')
        
        for thiskey1 in vacation:
            if "Ferieplan" in vacation[thiskey1]:
                return Vacationloop()     
            else:
                break
            
        for thiskey2 in vacation:
            if "Kr. Himmelfartsferie" in vacation[thiskey2]:
                kristi1 = vacation["vacationtype"]
                kristi2 = kristi1.split(' - ')
                kristi3 = kristi2[0]
                ed1 = kristi2[1]
                kristi4 = kristi3.split(' torsdag ')
                vt = kristi4[0]
                sd1 = kristi4[1]
                vacation["vacationtype"] = vt
                vacation["startdate"] = "torsdag " + sd1
                vacation["enddate"] = ed1
                myvacationlist.append(vacation)
                return Vacationloop()  
            else:
                break
            
        for thiskey3 in vacation:
            if "Undervisningsministeriets" in vacation[thiskey3]:
                keeprunning.append("1")
                break 
            else:
                break
            
        if len(keeprunning) == 1:
            break
            
        datoline = myFile.readline()
        datoparts = datoline.split(' - ')
        sd = datoparts[0]
        
        if len(datoparts) == 2:
            ed = datoparts[1]
        else:
            ed = sd
            
        vacation["startdate"] = sd.strip().strip(')(')
        vacation["enddate"] = ed.strip().strip(')(')
        
        myvacationlist.append(vacation)

Vacationloop()

print(myvacationlist)
