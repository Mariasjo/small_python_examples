# -*- coding: utf-8 -*-
'''
Created on 06/12/2012

@author: Maria
'''

import tkinter as tk

def result():
    print( " this sum of 2+2 is : ", 2+2)

mainWindow = tk.Tk()
mainWindow = root.tk("Password Generator")    
    
win = tk.Frame()
win.pack()
label1 = tk.Label( win, text = "click New to create a new password.").pack(side=tk.TOP)
button1 = tk.Button( win, text = "New", command = result, cursor="plus").pack(side=tk.LEFT)
button2 = tk.Button( win, text = "Quit", command = win.quit).pack(side=tk.RIGHT)


win.mainloop()