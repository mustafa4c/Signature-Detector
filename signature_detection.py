### start DuplicateRemover img ###
from PIL import Image  
from DuplicateRemover import DuplicateRemover
### end DuplicateRemover img ###
### start upload img ###
from fileinput import filename
from tkinter import filedialog 
from PIL import Image,ImageTk
### end upload img ###
# Start Extract the image name 
import os
# End Extract the image name 
from distutils.cmd import Command
from tkinter import *
from tkinter.font import BOLD
from cProfile import label
from distutils.log import error
import errno
from fileinput import filename
from tkinter import *
import mysql.connector 
import tkinter as tk
from tkinter import filedialog 
from PIL import Image,ImageTk
from tkinter import messagebox
import io
import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np
from PIL import Image
import imagehash
import os
import numpy as np


Signature_validation=Tk()
Signature_validation.title("Admin Page")
Signature_validation.geometry('1200x700+150+50')
Signature_validation.configure(bg='#fff')
Signature_validation.resizable(False,False)

#*************************************************** Start Function Page **************************************************************

# ################### Def Upload Image #######################
def upload_image():
    global img 
    global image1
    f_types = [('png files', '*.png'), ('jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    if(filename):

        img = filename
        
        ### show img ###
        image1 = Image.open(img) 
        image1.show()


    else:
        messagebox.showwarning("showwarning", "Please choose the correct signature")

#################### Def Signature Validation #################
def star_Signature_validation():
    # cv2.waitKey(2000)

    class DuplicateRemover:
        def __init__(self,dirname,hash_size = 8):
            self.dirname = dirname
            self.hash_size = hash_size
            
                
        def find_similar(self,location,similarity=80):
            global nameimg
            fnames = os.listdir(self.dirname)
            threshold = 1 - similarity/100
            diff_limit = int(threshold*(self.hash_size**2))
            
            with Image.open(location) as img:
                hash1 = imagehash.average_hash(img, self.hash_size).hash
            
            print("Finding Similar Images to {} Now!\n".format(location))
            for image in fnames:
                with Image.open(os.path.join(self.dirname,image)) as img:
                    hash2 = imagehash.average_hash(img, self.hash_size).hash
                    
                    if np.count_nonzero(hash1 != hash2) <= diff_limit:
                        print("{} image found {}% similar to {}".format(image,similarity,location))

                         # Extract the image name 
                        nameimgpath = os.path.basename(image)
                        print(nameimgpath)

                        nameimg = os.path.splitext(nameimgpath)[0]
                        print(nameimg)

                    # else:
                    #     msg_box = tk.messagebox.askquestion('Exit Application', 'This signature is fake Do you want to add it to the table of fake signatures?')
                        
                    #     if msg_box == 'yes':
                    #         messagebox.showinfo("showinfo", "operation accomplished successfully")
                        
                    #     else:
                    #         tk.messagebox.showinfo('Return', 'Sir, always try to keep fake signatures')



                        
                      
    global img
    dirname = "DB_signature"

    # Remove Duplicates
    dr = DuplicateRemover(dirname)
    # dr.find_duplicates()

    # Find Similar Images
    dr.find_similar(img,93)


    try:
            connection = mysql.connector.connect(  
            host="localhost",
            user="root",
            password="00990099",
            database="signature")

            cursor = connection.cursor()
            sql_select_query = """select * from signature_customer where number_account = %s"""
            # set variable in query
            cursor.execute(sql_select_query, (nameimg,))
             # fetch result
            record = cursor.fetchall()

            
            my_w= Toplevel(Signature_validation)
            my_w.geometry('700x300+200+150')# size as width height
            my_w.title("User Data")

            
            # Column headers  row 0
            l1=Label(my_w, text='ID') 
            l1.grid(row=0,column=1) 

            l2=Label(my_w, text='Name') 
            l2.grid(row=0,column=2) 

            l3=Label(my_w, text='Account Number') 
            l3.grid(row=0,column=3) 

            l4=Label(my_w, text='Signature customer') 
            l4.grid(row=0,column=4)

            # l5=Label(my_w, text='Signature Check') 
            # l5.grid(row=0,column=5) 
                
            i=1 # data starts from row 1 
            images = [] # to manage garbage collection. 

            for customer in record: 
                    
                    
                    stream = io.BytesIO(customer[3])
                    img=Image.open(stream)
                    img=img.resize((200, 200))
                    img = ImageTk.PhotoImage(img)    


                    e = Label(my_w, text=customer[0]) 
                    e.grid(row=i,column=1,ipadx=20) 

                    e = Label(my_w, text=customer[1]) 
                    e.grid(row=i,column=2,ipadx=60) 

                    
                    e = Label(my_w, text=customer[2]) 
                    e.grid(row=i,column=3,ipadx=100) 

             
                    e = Label(my_w, image=img) 
                    e.grid(row=i, column=4,ipady=7)  
                    images.append(img) # garbage collection 

                    
                    # e = Label(my_w, image=img) 
                    # e.grid(row=i, column=5,ipady=7)  

                    i=i+1    
                    

    except mysql.connector.Error as error:
                print("Failed to get record from MySQL table: {}".format(error))
                print("yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeees")
                


    finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")

#*************************************************** End Function Page ****************************************************************

##################### Frame And Heading #####################
frame=Frame(Signature_validation,width=1200,height=200,bg='#fff')
frame.place(x=200,y=50)

heading=Label(frame,text='Signature Check',fg='#13bd87',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=200,y=5)

##################### Image #####################
img2 = PhotoImage(file='img/undraw_Credit_card_re_blml.png',width=1000,height=700)
Label(Signature_validation,image=img2,border=0,bg='white',width=900 ,height=550).place(x=480,y=130)

##################### Frame Entry #####################
frameEntry=Frame(Signature_validation,width=400,height=900,bg='#fff')
frameEntry.place(x=50,y=150)

#################### Upload Button ##############
Button(frameEntry,width=25,pady=5,text='Upload Signture',font=('Microsoft YaHei UI Light',13,'bold'),bg='#ddd',fg='#000',border=0,cursor='hand2', command=upload_image).place(x=30,y=220)

#################### Enter Button ##############
Button(frameEntry,width=25,pady=5,text='Verification',font=('Microsoft YaHei UI Light',13,'bold'),bg='#13bd87',fg='white',border=0,cursor='hand2' , command=star_Signature_validation).place(x=30,y=300)


Signature_validation.mainloop()