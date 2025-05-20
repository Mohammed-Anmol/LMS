from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def studentRegister():
    
    sid = studInfo1.get()
    sname = studInfo2.get()
    sname = sname.lower()
    
    insertstudent = "insert into student values('"+sid+"','"+sname+"',0)"
    try:
        cur.execute(insertstudent)
        con.commit()
        messagebox.showinfo('Success',"student added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(sid)
    print(sname)
    


    root.destroy()
    
def addstudent(): 
    
    global studInfo1,studInfo2,Canvas1,con,cur,studentTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    con = pymysql.connect(host="localhost",user="root",password="anmol",database="db")
    cur = con.cursor()

    # Enter Table Names here
    studenttable = "student" # student Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="orange")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Students", bg='white', fg='black', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='white')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="student id : ", bg='white', fg='black')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    studInfo1 = Entry(labelFrame)
    studInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="student name: ", bg='white', fg='black')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    studInfo2 = Entry(labelFrame)
    studInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='white', fg='black',command=studentRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
