from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
   
    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','available')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bid)
    print(title)
    print(author)
    print(status)


    root.destroy()
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "root"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password="password",database="db")
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="Grey")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="Black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='White', fg='Black', font=('Arial',17))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='white')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='white', fg='black', font=('Tahoma',8))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.50, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='white', fg='black',font=('Tahoma',8))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.50, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='white', fg='black',font=('Tahoma',8))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.50, relheight=0.08)
        
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='white', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()	

