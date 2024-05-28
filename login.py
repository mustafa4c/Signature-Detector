from cProfile import label
from email import header
from re import M
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import ast
import mysql.connector
from turtle import heading
from subprocess import call
import cv2

window=Tk()
window.title("SignUp")
window.geometry('1200x700+150+50')
window.configure(bg='#fff')
window.resizable(False,False)

##################### Functions #################

def submitact():
	cv2.waitKey(1000)
	Username = user.get()
	passw = code.get()

	print(f"The name entered by you is {user} {passw}")

	logintodb(Username, passw)


def logintodb(Username, passw):
	
	# If password is enetered by the
	# user
	if passw:
		db = mysql.connector.connect(host ="localhost",
									user = Username,
									password = passw,
									db ="signature")
		cursor = db.cursor()
		
	# If no password is enetered by the
	# user
	else:
		db = mysql.connector.connect(host ="localhost",
									user = Username,
									db ="signature")
		cursor = db.cursor()
		
		
	# A Table in the database
	savequery = "select * from signature_customer"
	
	try:
		cursor.execute(savequery)
		myresult = cursor.fetchall()
		
		# Printing the result of the
		# query
		for x in myresult:
			print(x)
		messagebox.showinfo("showinfo", "You are logged in successfully")
		call(["python", "Select_operation.py"])

		
	except:
		db.rollback()


##################### Image #####################
img = PhotoImage(file='img/undraw_Investment_data_re_sh9x.png',width=1400,height=694)
Label(window,image=img,border=0,bg='white',width=700 ,height=700).place(x=500,y=10)

##################### Frame And Heading #####################
frame=Frame(window,width=350,height=390,bg='#fff')
frame.place(x=100,y=230)

heading=Label(frame,text='Entry Data',fg='#13bd87',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=60,y=5)

##################### Username Entry #####################
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

##################### Password Entry #####################
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    if code.get()=='':
        code.insert(0,'Password')

sv = tk.StringVar()
e1_str=tk.StringVar()
code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11), show='*', textvariable=e1_str)
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

c_v1=IntVar(value=0)
def my_show():
    if(c_v1.get()==1):
        code.config(show='')
    else:
        code.config(show='*')


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##################### Signin Button #####################
Button(frame,width=39,pady=7,text='Sign in',bg='#13bd87',fg='white',border=0,cursor='hand2',command=lambda: [submitact()]).place(x=35,y=200)

window.mainloop()   