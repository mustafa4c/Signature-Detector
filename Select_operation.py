from tkinter import *
from tkinter.font import BOLD
from subprocess import call

page2=Tk()
page2.title("Admin Page")
page2.geometry('1200x700+150+50')
page2.configure(bg='#fff')
page2.resizable(False,False)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Start Function Page @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def add_page():
    call(["python", "signature_add.py"])

def validation_page():
    call(["python", "signature_detection.py"])

def show_data():
    call(["python", "show_data.py"])
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ End Function Page @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

##################### Frame And Heading #####################
frame=Frame(page2,width=1200,height=700,bg='#fff')
frame.place(x=200,y=100)

heading=Label(frame,text='Please Choose the Type of Operation',fg='#13bd87',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=60,y=5)

##################### Image #####################
img = PhotoImage(file='img/undraw_Vault_re_s4my (2).png',width=1400,height=504)
Label(page2,image=img,border=0,bg='white',width=900 ,height=500).place(x=450,y=150)

#################### Select Button ##############
Button(page2,width=35,pady=10,text='Add New Signture',font=('Microsoft YaHei UI Light',12,'bold'),bg='#13bd87',fg='white',border=0,cursor='hand2',command=add_page).place(x=50,y=350)

Button(page2,width=35,pady=10,text='Signature validation',font=('Microsoft YaHei UI Light',12,'bold'),bg='#13bd87',fg='white',border=0,cursor='hand2', command=validation_page).place(x=50,y=450)

Button(page2,width=35,pady=10,text='Show Data',font=('Microsoft YaHei UI Light',12,'bold'),bg='#13bd87',fg='white',border=0,cursor='hand2', command=show_data).place(x=50,y=550)


page2.mainloop()