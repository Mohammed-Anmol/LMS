from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code


con = pymysql.connect(host="localhost",user="root",password="password",database="db")
cur = con.cursor()

# Enter Table Names here
studenttable = "student" 
    
def sview(): 
    
    root = Tk()
    root.title("Student Details")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="Purple")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Books", bg='white', fg='black', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='white')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="%-10s%-40s%-30s"%('SID','Student name','No.of Books'),bg='white',fg='black').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------",bg='white',fg='black').place(relx=0.05,rely=0.2)
    getstudents = "select * from student"
    try:
        cur.execute(getstudents)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-30s%-30s"%(i[0],i[1],i[2]),bg='white',fg='black').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()