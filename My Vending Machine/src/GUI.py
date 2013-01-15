'''
Created on 20/12/2012

@author: Maria
'''
def Input1kr():
    myVM.inputEvent(VM.Coin_1)
    

def showGUI():
    mainWindow = tk.Tk()
    mainWindow.title("Vending Machine")
# Create a frame to hold all the GUI elements
    win = tk.Frame(mainWindow)

    creditVar = tk.StringVar()
    creditVar 

    displayTextVar = tk.StringVar()
    displayTextVar.set('Starting')
    win.pack()
    
    labelDisplay = tk.Label(win, textvariable=displayTextVar).pack(side=tk.TOP)
    button1 = tk.Button( win, text = "1 kr.", command = Input1kr()).pack(side=tk.TOP)
    win.mainloop()
   

import tkinter as tk

import VendingMachine as VM

if __name__ == '__main':
    myVM = VM.VendingSM()
    
    showGUI()

#import VendingMachine as VM
#mainWindow = tk.Tk()
#mainWindow.title("Vending Machine")
#mainWindow.minsize(300, 100)
#mainWindow.resizable(width=False, height=False)    

# Create a frame to hold all the GUI elements

#win = tk.Frame(mainWindow, width=300, height=100)
#win.pack()

# StringVar is the connection from the GUI to the code in this file
# Update them with .set in the callback functions  
#resultVar = tk.StringVar()
#resultVar.set("")

#win.pack()
#label1 = tk.Label( win, textvariable=textVar).pack(side=tk.TOP)
#button1 = tk.Button( win, text = "1 kr.", command = result).pack(side=tk.TOP)
#button2 = tk.Button( win, text = "2 kr.", command = result).pack(side=tk.TOP)
#button3 = tk.Button( win, text = "5 kr.", command = result).pack(side=tk.TOP)
#button4 = tk.Button( win, text = "10 kr.", command = result).pack(side=tk.TOP)
#button5 = tk.Button( win, text = "20 kr.", command = result).pack(side=tk.TOP)
#buttoncancel = tk.Button( win, text = "20 kr.", command = result).pack(side=tk.TOP)
#button2 = tk.Button( win, text = "Quit", command = win.quit).pack(side=tk.RIGHT)
#textEntry1 = tk.Entry( win,  textvariable=resultVar).pack(side=tk.BOTTOM)


#win.mainloop()