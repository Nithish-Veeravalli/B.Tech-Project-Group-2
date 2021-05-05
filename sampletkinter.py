#import sys
import os
#import subprocess
import tkinter
#import tkinter.messagebox
import tkinter.filedialog
top = tkinter.Tk()


def helloCallBack():
   top.filename = tkinter.filedialog.askopenfilename(initialdir="/downloads",title="")
   command = "C:/Users/ASUS/Desktop/Spice64/bin/ngspice "+ top.filename
   #command = "cmd /k cd C:/Users/ASUS/Desktop/Spice64/bin/ngspice.exe"
   print(command)
   #os.system(command)
   #os.system("cmd /k ngspice.exe")
   os.system(command)
   

B = tkinter.Button(top, text ="pick", command = helloCallBack)
L= tkinter.Label(text="Welcome to Tkinter!! pick a file", fg="Red", font=("Helvetica", 16))

L.pack()
B.pack()
top.wm_title("File Picker") 
top.geometry("200x100")
top.mainloop()




