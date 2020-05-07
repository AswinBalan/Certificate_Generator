from tkinter import *
from tkinter import messagebox  

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import os
from tkinter.font import Font
from functools import partial
from reportlab.pdfgen import canvas

from reportlab.lib.pagesizes import letter
import pyqrcode
import math
import png
import urllib
from datetime import datetime
from pyqrcode import QRCode
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

import uuid
import itertools
import json
import openpyxl


#   backend code

def draw(rows,temp,domain,total,singlestudent):
    out_of = total
    print(out_of)


    candidateName="Default"
    day= None
    d_name = None

    # Getting Date from timestamp
    date = rows[0][-2].split()[0]
    

    domain_list = []
    json_data = {}

    # Change d_name to candidateName, if for singlestudent
    if singlestudent == 1:
        d_name = rows[0][0]
    else:
        d_name = domain
        with open('./json/confdata_'+str(date)+'.json','a') as f:
            pass

    # Removing Spaces
    d_name = d_name.strip().replace(" ",'_')

    os.mkdir("./Certificates/Certificate_"+d_name+"_"+str(date).strip())
    
    # Static Values - Can be change after implementing Advanced
    x = [340, 385,480]
    y = [311, 169,124]

    for row in rows:
            user_info = {}
            i = -1
            j= 0
            # Candidate Name
            candidateName = row[0].strip()
            # Init - Canvas
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)

            # parsing each column of a row 
            for col in row[:-1]:
                # Iterables
                    i = i + 1
                    j = j+1
                    print(col,"\n") 
                    # Converting Score to Percentage of Second Column
                    if j == 2:
                          col = str(round(int(col)/int(out_of)*100))+"%"
                          print(col)

                    can.setFont('Times-Italic', 22)

                    # Changing Date format and getting day
                    if col == row[-2]:
                        col = datetime.strptime(col.split()[0], '%Y-%m-%d').strftime('%d-%m-%Y')
                        day= col
                        print(col)
                        
                    # Draw at locations
                    can.drawString(x[i], y[i], col)
            
            # Writing Domain Name
            can.drawString(490,285,domain)

            #Generate Unique Id
            UUID = uuid.uuid1()
            
##          Encrypted Information in QR            

            s = "https://smveczilla.in/cverify.html?id="+str(UUID)+"&email="+row[-1].lower()+"&valid="+day.split('-')[0]
            
            # Writing Encrypted Information
            url = pyqrcode.create(s)
            url.png('myqr.png', scale = 2) 
            can.drawImage('./myqr.png',650,117,100,100)
            can.save()
            
            #move to the beginning of the StringIO buffer
            packet.seek(0)
            new_pdf = PdfFileReader(packet)
            # read your existing PDF
            existing_pdf = PdfFileReader(open(temp, "rb"))
            output = PdfFileWriter()
            # add the "watermark" (which is the new pdf) on the existing page
            page = existing_pdf.getPage(0)
            page.mergePage(new_pdf.getPage(0))
            output.addPage(page)

            # generating the certificates

            outputStream = open("./Certificates/Certificate_"+d_name+"_"+str(date).strip()+"/"+row[-1].lower().split('@')[0]+"_Certificate.pdf", "wb")
            output.write(outputStream)
            outputStream.close()
            
            # Preparing for JSON file
            user_info["Name"] = candidateName
            user_info["Email"] = row[-1].lower()
            user_info["UUID"] = str(UUID)
            user_info["url"] = ""
            user_info["C_date"] = row[-2]
            domain_list.append(user_info)
            # if True:
            #    break
    json_data[domain.strip().replace(" ",'_')] = domain_list
    

    # Writing to the JSON file

    date = str(date).strip()
    if singlestudent == 0:
        # Multiple Students
        try:
            with open('./json/confdata_'+date+'.json','r') as f:
                reload = json.load(f)
        except json.decoder.JSONDecodeError as e:
            print(e)
            reload ={}
        reload.update(json_data)
        json_object = json.dumps(reload, indent = 6) 
        with open('./json/confdata_'+date+'.json','w') as af:
            af.write(json_object)
    else:

        # Single student
        dict_init = {}
        dict_init.update(json_data)
        json_object = json.dumps(dict_init, indent=6)

        with open('./json/'+d_name+"_"+date+'.json','w') as sf:
            sf.write(json_object)
    
    messagebox.showinfo("Information","Certificates Generated Successfully and Stored Under Certificates!")
