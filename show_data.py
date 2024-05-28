import mysql.connector
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("1200x600")
my_connect = mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="00990099",
  database="signature"
)
my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM signature_customer ORDER BY id DESC")
i=0 
for signature_customer in my_conn: 
    for j in range(len(signature_customer)):
        e = Entry(my_w, width=50, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, signature_customer[j])
    i=i+1
    print(signature_customer)
my_w.mainloop()