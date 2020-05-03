from tkinter import *
from tkinter import filedialog
from functools import partial


pathlabel1 = None
temp = None
option = None
nameEntry = None
btnName1 = None
btnName2 = None

def btnfn1(frame):
    from home import homeFunction
    frame.destroy()
    homeFunction()

def btnfn2(temp,domain):
    entry_list  = []
    from drawing import draw
    for i in nameEntry[:-1]:
        entry_list.append(i.get())
    list = []
    list.append(entry_list)
    print("List",list)
    total = nameEntry[-1].get()
    print("Total",total)
    draw(list,temp,domain,total,1)
    pass

def clearAll():
    for i in nameEntry:
        i.delete(0,'end')
    pathlabel1['text']=""
    option.set('Photoshop')
    btnName1.destroy()
    btnName2.destroy()


def btnfn4(frame):
    print('yet to implement')
    pass


def template_fn(frame,option):
    filename = filedialog.askopenfilename()
    pathlabel1.config(text=filename)
    global temp, btnName1, btnName2
    # Getting Template file Name
    temp = filename

    btnFunction2 = partial(btnfn2,temp,option.get())
    btnName1 = Button(frame,text="Generate Certificate",command=btnFunction2,width=15)
    btnName1.place(x=390,y=550)
  
    btnFunction4 = partial(btnfn4,frame)
    btnName2 = Button(frame,text="Advanced",command=btnFunction4,width=15)
    btnName2.place(x=650,y=550)


def clear(entryObj):
        entryObj.delete(0,'end')

def singleFunction(frame, root):

    global nameEntry
    nameList = ["Full Name","Score","Time Stamp (yyyy-mm-dd hh:mm:ss)","Email"]
    buttonList = ["Home","Generate Certificate","Resert", "Advanced"]
    nameEntry = []
    y = 150
    frame = Frame(root,width=900, height=600, bg="lightblue")
    frame.pack()

    # Title Label
    titleLabel= Label(frame,text="Single Student",font=("Times", "24", "bold italic"),bg="lightblue",fg="green")
    titleLabel.place(x=350,y=50)
    
    for i in range(len(nameList)):
        add = 0
        var = StringVar(frame)
        var1 = StringVar(frame)
        var1.set("10")

        if i == 1:
            add = 20
            special = Entry(frame,textvariable=var1, width=35-add)
            special.place(x=520,y=y)
        
        nameLabel = Label(frame,text=nameList[i],width=35)
        nameLabel.place(x=50,y=y)

        obj = Entry(frame,textvariable=var, width=35-add)
        obj.place(x=400,y=y)
        nameEntry.append(obj)
        
        # print(nameEntry)
        
        clearMe = partial(clear,nameEntry[i])
        clearbtn = Button(frame,text="Clear",width=10,command=clearMe)
        clearbtn.place(x=650,y=y)
        
        y = y + 50
    nameEntry.append(special)
    menulabel = Label(frame,text="Choose Domain name",width=35)
    menulabel.place(x=50,y=353)
    global option
    option = StringVar(frame)
    option.set("Photoshop")
    menu = OptionMenu(frame,option,"Photoshop","C Programming", "Python Programming")
    menu.place(x=400,y=350)

    templateFile = Label(frame,text="Choose the Template (.pdf)",width=35)
    templateFile.place(x=50,y=453)

    new_fn = partial(template_fn,frame,option)
    browsebutton2 = Button(frame, text="Browse", command=new_fn,width=15)
    browsebutton2.place(x=400,y=450)

    # Hope User is filling form in ordered manner, so
     
    global pathlabel1
    pathlabel1 = Label(frame)
    pathlabel1.place(x=550,y=453)

    # Label '/' represents out of
    outofLabel = Label(frame,text="/")
    outofLabel.place(x=500,y=200)

    btnFunction1 = partial(btnfn1,frame)
    btnName = Button(frame,text="Home",command=btnFunction1,width=15)
    btnName.place(x=50,y=550)

    # clear_part = partial(clearAll,btnName1, btnName2)
    btnName = Button(frame,text="Reset",command=clearAll,width=15)
    btnName.place(x=510,y=550)



    print("Success")