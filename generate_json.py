from tkinter import *
from tkinter import filedialog
from tkinter import messagebox 

from functools import partial
import time
import itertools
import json

from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 
import os 

pathlabel = None
filename = None
entryList = None

def btnfn1(frame):
    frame.destroy()
    from home import homeFunction
    homeFunction()



def id_fn(entryList):
    print(entryList)
    internet = {}
    dic ={}
    inter= []
    gauth = GoogleAuth() 
    gauth.LocalWebserverAuth()	 
    drive = GoogleDrive(gauth)
    for i in entryList:
        links = []
        fileList = drive.ListFile({'q': "'{}' in parents and trashed=false".format(i.get())} ).GetList()
        for f in fileList:
            d= {}
            d['Email']=f['title']
            url = "https://drive.google.com/open?id="+f['id']
            d['url'] = url
            links.append(d)
        inter.append(links)

    print(inter)
    with open(filename,'r') as f:
        local = json.load(f)

    domain =["Photoshop","Python_Programming","C_Programming"]

    for (i,dn) in zip(inter,domain):
        internet[dn]=i


    # Merging JSON files
    for (key,value), (key2,value2) in zip(internet.items(), local.items()):
        for each1 in value:
            for each2 in value2:    
                if each2['Email'].split('@')[0]+"_Certificate.pdf" == each1['Email']:
                            print("Yes")
                            each2['url'] = each1['url']

    # Checker
    print(local["Photoshop"])

    json_final = json.dumps(local, indent = 6) 
    with open(filename,'w') as af:
        af.write(json_final)

    messagebox.showinfo("Information","JSON Updated Successfully and stored under JSON Folder")
    


def clearAll():
    for i in entryList:
        i.delete(0,'end')
    pathlabel['text']=""


def browse(frame):
    global filename
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)

    new_fn = partial(id_fn,entryList)
    browsebutton2 = Button(frame, text="Generate", command=new_fn,width=15)
    browsebutton2.place(x=400,y=450)

def automate(frame,root):
    global entryList
    entryList = []

    frame = Frame(root,width=900, height=600, bg="lightblue")
    frame.pack()
    
        # Title Label
    titleLabel= Label(frame,text="JSON Generation",font=("Times", "24", "bold italic"),bg="lightblue",fg="green")
    titleLabel.place(x=300,y=50)
    
    labelList =["Photoshop Folder ID","Python Folder ID", "C Folder ID"]

    y = 150
    for i in labelList:
            var1 = StringVar(frame)

            fileIDLabel = Label(frame,text=i,width=25)
            fileIDLabel.place(x=100,y=y)
            fileIDEntry = Entry(frame,textvariable=var1, width=45)
            fileIDEntry.place(x=400,y=y) 
            entryList.append(fileIDEntry)
            y = y + 50

    browseLabel = Label(frame,text="Choose JSON file to update", width=25)
    browseLabel.place(x=100,y=y)

    browse_part = partial(browse,frame)
    browsebutton1 = Button(frame, text="Browse", command=browse_part,width=15)
    browsebutton1.place(x=400,y=y)

    global pathlabel
    pathlabel = Label(frame)
    pathlabel.place(x=550,y=y)

    btnFunction1 = partial(btnfn1,frame)
    btnName = Button(frame,text="Home",command=btnFunction1,width=15)
    btnName.place(x=100,y=450)

    btnName = Button(frame,text="Reset",command=clearAll,width=15)
    btnName.place(x=560,y=450)
