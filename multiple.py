from tkinter import *
from tkinter import filedialog
from functools import partial


var = None
var1 = None
xlsx_filename = None
fields = None
pathlabel1 = None 
pathlabel2 = None


def advanced():
    print("Yet to implement")

def browsefunc1():
    global xlsx_filename

    filename = filedialog.askopenfilename()
    pathlabel1.config(text=filename)

    #store for future
    xlsx_filename = filename


def browsefn2(frame):
    from certificate_generator import generate
    tmp_filename = filedialog.askopenfilename()
    pathlabel2.config(text=tmp_filename)
    print(var.get())

    action_with_arg = partial(generate ,tmp_filename,xlsx_filename,var.get(), var1.get())
    button = Button(frame,width=17, text="Generate Certificates", command=action_with_arg)
    button.place(x=300,y=500)

    button = Button(frame,width=17, text="Advanced", command=advanced)
    button.place(x=500,y=500)


def callhome(frame):
    frame.destroy()
    from home import homeFunction
    homeFunction()

def multipleFunction(frame,root):

    global pathlabel1, pathlabel2, var, var1

    frame = Frame(root,width=900, height=600, bg="lightblue")
    frame.pack()

    # Title Label
    titleLabel= Label(frame,text="Multiple  Students",font=("Times", "24", "bold italic"),bg="lightblue",fg="green")
    titleLabel.place(x=350,y=50)

    # SET 1
    browsebutton1 = Button(frame,width=15, text="Browse", command=browsefunc1)
    browsebutton1.place(x=300,y=150)

    csvFile = Label(frame,width=25,text="Choose the Name List (.xlsx)")
    csvFile.place(x=30,y=153)

    pathlabel1 = Label(frame)
    pathlabel1.place(x=500,y=153)

    #SET2
    browsefunc2 = partial(browsefn2,frame)
    browsebutton2 = Button(frame,width=15, text="Browse", command=browsefunc2)
    browsebutton2.place(x=300,y=350)

    templateFile = Label(frame,width=25,text="Choose the Template (.pdf)")
    templateFile.place(x=30,y=353)

    pathlabel2 = Label(frame)
    pathlabel2.place(x=500,y=353)

    # Option Menu

    var = StringVar(frame)
    var.set("Photoshop")

    menulabel = Label(frame,text="Choose Domain name",width=25)
    menulabel.place(x=30,y=203)

    menu = OptionMenu(frame,var,"Photoshop","C Programming", "Python Programming")
    menu.place(x=300,y=200)

    var1= StringVar(frame)
    var1.set("10")

    label = Label(frame,text="Total Score",width=25)
    label.place(x=30,y=303)
    entry = Entry(frame,textvariable=var1,width=18)
    entry.place(x=300,y=300)

    call_partial = partial(callhome,frame)

    homebutton = Button(frame,width=17, text="Home", command=call_partial)
    homebutton.place(x=50,y=500)


