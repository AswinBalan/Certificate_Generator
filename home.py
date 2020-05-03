from tkinter import *
from tkinter import filedialog
from functools import partial
# Calling user defined modules
from single import singleFunction
from multiple import multipleFunction
from generate_json import automate
# Initializing Global variables
frame = None
root = None



def NextPage1(frame):
    # Frame Destroyed

    frame.destroy()
    print("Frame1 Destroyed")
    singleFunction(frame, root)

    
def NextPage2(frame):
    # Frame Destroyed
    frame.destroy()
    print("Frame2 Destroyed")
    multipleFunction(frame, root)


def filefn(frame):
    frame.destroy()
    automate(frame,root)

def homeFunction():
# Make it as global
    global frame
    global root

    frame = Frame(root,width=900, height=600, bg="gray")
    frame.pack()

    # Title Label
    titleLabel= Label(frame,text="Home Page",font=("Times", "24", "bold italic"),bg="gray",fg="green")
    titleLabel.place(x=350,y=50)
    # Label 

    singleLabel = Label(frame,text="Cerate Certificate For",width=25)
    singleLabel.place(x=325,y=150)

    # Calling Single Button
    callMe = partial(NextPage1 ,frame)
    singlebtn = Button(frame,text="Single Student", command=callMe,width=15)
    singlebtn.place(x=360,y=200)

# Muliple User Label
    multipleLabel = Label(frame,text="Or",width=25)
    multipleLabel.place(x=325,y=250)

#  Calling Multiple Button
    callMe = partial(NextPage2 ,frame)    
    multipleButton = Button(frame,text="Multiple Students",command=callMe,width=15)
    multipleButton.place(x=360,y=300)

# Final JSON FIle Generation

    multipleLabel = Label(frame,text="Click to Generate Final JSON File. Note: Only after uploading certificates to Drive",font=("Times", "14", "bold italic"),fg="green")
    multipleLabel.place(x=100,y=400)

    callMe = partial(filefn ,frame)    
    jsonbtn = Button(frame,text="Create JSON",command=callMe,width=15)
    jsonbtn.place(x=360,y=500)

# Running the GUI infinitely


if __name__ == "__main__":
    root = Tk()
    root.title("Home")
    homeFunction()
    root.minsize(900,600)
    root.resizable(0,0)
    root.mainloop()
    pass