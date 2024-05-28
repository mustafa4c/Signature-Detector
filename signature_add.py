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
import cv2

page3=Tk()
page3.title("Admin Page")
page3.geometry('1200x700+150+50')
page3.configure(bg='#fff')
page3.resizable(False,False)

#*************************************************** Start Function Page **************************************************************

# ################### Def Upload Image #######################
def upload_image():
    global filename,img 
    global filename,image 
    f_types = [('png files', '*.png'), ('jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    if(filename):

      img = filename

      ### show img ###
      image = Image.open(img) 
      image.show()



    
    else:
        messagebox.showwarning("showwarning", "Please choose the correct signature")

##################### Def Sign_in ############################
def submit():
  fb = open(filename, 'rb')
  fb = fb.read()

  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="00990099",
  database="signature"
)
  try:
    mycursor = mydb.cursor()

    sql = "INSERT INTO signature_customer (name, number_account, signature) VALUES (%s, %s, %s)"
    val = [(user.get(),numAccount.get(), fb)]
    mycursor.executemany(sql, val)
    mydb.commit()
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    messagebox.showinfo("showinfo", "record inserted.")

    image = Image.open(img) 
    
    path  = "DB_signature"
    x = numAccount.get()+'.png'

    ### save img ###
    image = image.save('{}/{}'.format(path,x))

  except mysql.connector.Error as error:
    messagebox.askretrycancel("askretrycancel", "falid to insert into table {}".format(error))

  finally:
    if mydb.is_connected():
       mycursor.close()
       mydb.close()
       print("Mysql connection is closed")

    else:
        messagebox.askretrycancel("askretrycancel", "Try again?")

#*************************************************** End Function Page ****************************************************************

##################### Frame And Heading #####################
frame=Frame(page3,width=1200,height=200,bg='#fff')
frame.place(x=200,y=50)

heading=Label(frame,text='Enter Customer Data',fg='#13bd87',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=200,y=5)

##################### Image #####################
img2 = PhotoImage(file='img/undraw_Online_payments_re_y8f2 (1).png',width=1150,height=700)
Label(page3,image=img2,border=0,bg='white',width=900 ,height=700).place(x=280,y=100)

##################### Frame Entry #####################
frameEntry=Frame(page3,width=300,height=400,bg='#fff')
frameEntry.place(x=50,y=150)

##################### Username Entry #####################
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user = Entry(frameEntry,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=150)
user.insert(0,'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frameEntry,width=295,height=2,bg='black').place(x=25,y=107)

##################### Account Number Entry #####################
def on_enter(e):
    numAccount.delete(0,'end')

def on_leave(e):
    if numAccount.get() =='':
        numAccount.insert(0,'Account Number')

numAccount = Entry(frameEntry,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
numAccount.place(x=30,y=80)
numAccount.insert(0,'Account Number')
numAccount.bind("<FocusIn>",on_enter)
numAccount.bind("<FocusOut>",on_leave)

Frame(frameEntry,width=295,height=2,bg='black').place(x=25,y=180)

#################### Upload Button ##############
Button(frameEntry,width=20,pady=5,text='Upload Signture',font=('Microsoft YaHei UI Light',10,'bold'),bg='#ddd',fg='#000',border=0,cursor='hand2', command=upload_image).place(x=70,y=220)

#################### Enter Button ##############
Button(frameEntry,width=25,pady=5,text='Sing in',font=('Microsoft YaHei UI Light',13,'bold'),bg='#13bd87',fg='white',border=0,cursor='hand2' , command = submit ).place(x=30,y=300)
page3.mainloop()