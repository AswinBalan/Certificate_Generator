from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import os
from tkinter.font import Font
from functools import partial
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import csv
import pyqrcode 
import png 
from pyqrcode import QRCode
##filename = "./sample.csv"
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pathlib import Path
home = str(Path.home())
root = Tk()
root.title("Certificate Generator")

customFont = Font(family="Times New Roman", size=15, slant="italic")
label = Label(root, text="Certificate Generator", font=customFont,fg="red")
label.place(x=225,y=5)


def getEntry(obj1, filename,csv_filename):
    x= []
    y= []
    data_points = []
    for i in obj1:
        data_points.append(i.get())
    print(data_points)
    for i in data_points:
        a,b = map(int,i.split())
        x.append(a)
        y.append(b)
            
    rows = [] 
    fields= []
    flag  = -1
    # reading csv file 
    with open(csv_filename, 'r') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
            
            # extracting field names through first row 
            fields = next(csvreader) 
            for field in fields:
                if field in ["Marks","Percentage","Mark","Score","Scores","Percentages","marks","mark"]:
                    flag = fields.index(field)
            # extracting each data row one by one 
            for row in csvreader: 
                    rows.append(row) 

    
    print(len(fields))
    candidateName="Default"
##    sizes =[22,22,22,22]
    global finallabel
##    x = [400, 570, 550,150]
##    y = [200, 335, 215,548]
    os.mkdir(home+"/Downloads/Certificates")
    for row in rows:
            info=[]
            with open("../data.txt","r") as f:
                    uid = f.read()
                    print(uid)
                    f.close()
            i = -1
            candidateName = row[0]
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            # parsing each column of a row 
            for col in row:
                    i = i + 1
                    print(col,"\n") 
                    if flag == row.index(col):
                        col = str(col)+"%"
                    # create a new PDF with Reportlab
                    info.append(col)
                    can.setFont('Times-Italic', 22)
                    #CHANGE ACCORDING TO TEMPLATE
                    can.drawString(x[i], y[i], col)
            info.append(uid)
            uid = int(uid) + 1
            s = "It is a valid certificate produced by the our institute"+str(info)
            url = pyqrcode.create(s) 
            url.png('myqr.png', scale = 6) 
            can.setFillColorRGB(128, 128, 128) 
            can.drawImage('./myqr.png',650,117,100,100)
            can.save()
            #move to the beginning of the StringIO buffer
            packet.seek(0)
            new_pdf = PdfFileReader(packet)
            # read your existing PDF
            existing_pdf = PdfFileReader(open(filename, "rb"))
            output = PdfFileWriter()
            # add the "watermark" (which is the new pdf) on the existing page
            page = existing_pdf.getPage(0)
            page.mergePage(new_pdf.getPage(0))
            output.addPage(page)
            # finally, write "output" to a real file
            
            outputStream = open(home+"/Downloads/Certificates/"+candidateName+"_Certificate.pdf", "wb")
            output.write(outputStream)
            outputStream.close()
            with open("../data.txt","w") as f:
                    f.write(str(uid))
                    print(uid)
                    f.close()
            
    finallabel = Label(root, text="Certificates Generated Successfully. See Certificates Folder!", font=customFont,fg="green")
    finallabel.place(x=30,y=460)
    
   
def browsefunc1():
    iter=100
    global csv_filename
    global fields
    filename = filedialog.askopenfilename()
    pathlabel1.config(text=filename)
    print(filename)
    rows = [] 
    
    with open(filename, 'r') as csvfile:  
            csvreader = csv.reader(csvfile) 
            fields = next(csvreader) 
  

    #store for future
    csv_filename = filename
    print(fields)        

def browsefunc2():
    iter = 100
    filename = filedialog.askopenfilename()
    pathlabel2.config(text=filename)
    data=[]
    coordinate=[]
    new_val=[]
    global finallabel
##    finallabel =Label()
    #default values
    x = [340, 380, 480,470 ]
    y = [311, 169, 124,285 ]
    names=fields
    
    print(fields)
    for i in range(len(fields)):
            iter = iter + 50
            coordinateLabel = Label(root, text=names[i] + " Co-ordinate (x y)")
            coordinateLabel.place(x=30,y=iter)
            
            new_val.append(StringVar(root, value=str(x[i])+" "+str(y[i])))
            
            coordinateEntry =Entry(root, textvariable=new_val[i])
            coordinateEntry.place(x=225,y=iter, width=225, height=20)
            
            coordinate.append(coordinateEntry)
            
    action_with_arg = partial(getEntry, new_val,filename,csv_filename)
    button = Button(root, text="Generate_Certificates", command=action_with_arg)
    button.place(x=170,y=iter+50)

    clear_text = partial(clear_me,coordinate)
    clearbutton = Button(root, text="Clear", command=clear_text)
    clearbutton.place(x=300,y=iter+50)


def clear_me(entries):
    for entry in entries:
        entry.delete(0,'end')
    finallabel.config(text='')
    
    
#SET1
browsebutton1 = Button(root, text="Browse", command=browsefunc1)
browsebutton1.place(x=225,y=50)

csvFile = Label(root,text="Choose the Name List (.csv)")
csvFile.place(x=30,y=53)

pathlabel1 = Label(root)
pathlabel1.place(x=300,y=50)

#SET2

browsebutton2 = Button(root, text="Browse", command=browsefunc2)
browsebutton2.place(x=225,y=100)


templateFile = Label(root,text="Choose the Template (.pdf)")
templateFile.place(x=30,y=103)


pathlabel2 = Label(root)
pathlabel2.place(x=300,y=100)

            
root.minsize(600,500)
root.mainloop()
