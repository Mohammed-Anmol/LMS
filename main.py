from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from availablebookslist import *
from IssueBook import *
from ReturnBook import *
from issuedbookslist import *
from viewstudents import *
from addstudent import *

con = pymysql.connect(host="localhost",user="root",password="anmol",database="db")
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x700")

# Take n greater than 0.25 and less than 5
same=True
n=0.25

Canvas1 = Canvas(root)
Canvas1.config(bg="Brown")
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="brown",bd=5)
headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="East point institute \n Library management system", bg='white', fg='black', font=('Arial',14))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=0.8)

btn1 = Button(root,text="Add Book Details",bg='white', fg='brown', font=('Tahoma',11), command=addBook)
btn1.place(relx=0.28,rely=0.2, relwidth=0.45,relheight=0.09)
    
btn2 = Button(root,text="Available Book List",bg='white', fg='brown',font=('Tahoma',11) , command=View)
btn2.place(relx=0.28,rely=0.29, relwidth=0.45,relheight=0.09)

btn3 = Button(root,text="Issued Book List",bg='white', fg='brown',font=('Tahoma',11) , command=iview)
btn3.place(relx=0.28,rely=0.38, relwidth=0.45,relheight=0.09)

btn4 = Button(root,text="Add student",bg='white', fg='brown', font=('Tahoma',11), command = addstudent)
btn4.place(relx=0.28,rely=0.47, relwidth=0.45,relheight=0.09)

btn5 = Button(root,text="View student list",bg='white', fg='brown', font=('Tahoma',11), command = sview)
btn5.place(relx=0.28,rely=0.56, relwidth=0.45,relheight=0.09)
    
btn6 = Button(root,text="Issue Book to Student",bg='white', fg='brown',font=('Tahoma',11) , command = issueBook)
btn6.place(relx=0.28,rely=0.65, relwidth=0.45,relheight=0.09)
    
btn7 = Button(root,text="Return Book",bg='white', fg='brown', font=('Tahoma',11), command = returnBook)
btn7.place(relx=0.28,rely=0.74, relwidth=0.45,relheight=0.09)

btn8 = Button(root,text="Delete Book",bg='white', fg='brown', font=('Tahoma',11), command=delete)
btn8.place(relx=0.28,rely=0.83, relwidth=0.45,relheight=0.09)

root.mainloop()


