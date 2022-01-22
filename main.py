from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkinter import filedialog
from fpdf import FPDF
from db import Database
import datetime


db=Database("students.db")
#functions
def empty():
        a=0
        b=False
        try:
                for i in txtad.get(0.1,"end-1c"):
                        if i==" " or i=="\n":
                                a+=1
                if a==len(txtad.get(0.1,"end-1c")):
                        b=True
        except TypeError:
                b=True
        return b
def generatepdf(event):
        try:
                selectedrow=t2.focus()				
                data=t2.item(selectedrow)				
                global row1				
                row1=data["values"]
                ans=askyesno(title="Download",message="Do You Want To Download Student Details?")
                if ans:
                        lis=["student ID : ","Name : ","Age : ","Gender : ","Date Of Admission : " ,"Student No. : ","Parents No. : ","Address : ","Quota : "]
                        content=""
                        for i in range(len(lis)):
                                content+=lis[i]
                                content+=str(row1[i])
                                content+="\n"
                        pdf=FPDF()				
                        pdf.add_page()				
                        pdf.set_font('Arial','B',16)

                        pdf.multi_cell(w=100,h=10,txt=content,align='J')
                        filename=filedialog.askdirectory()
                        filename+='/'
                        filename+=row1[1]
                        filename+=".pdf"
                        pdf.output(filename,dest='F').encode('latin-1')
                        messagebox.showinfo("Sucess","Downloaded Successfully")
        except IndexError:
                messagebox.showinfo("Sorry","Heading Can't Downloaded")
        return

def datecheck():
    
    a=True
    try:
        day,month,year=txtdoa.get().split('/')
        datetime.datetime(int(year),int(month),int(day))
    except ValueError:
        a=False
    return a
def check():
    a=False
    if not (txtage.get().isdigit() or len(txtage.get())==2)or not datecheck():
        a=True
    elif not (txtsno.get().isdigit  and  len(txtsno.get())==10):
        a=True
    elif not (txtpno.get().isdigit  and  len(txtpno.get())==10):
        a=True
    return a
def getdata(event):
        
        selectedrow=t.focus()		
        data=t.item(selectedrow)		
        global row		
        row=data["values"]		
        name.set(row[1])		
        age.set(row[2])		
        doa.set(row[4])		
        gender.set(row[3])		
        sno.set(row[5])		
        pno.set(row[6])		
        txtad.delete(1.0,END)		
        txtad.insert(END,row[7])		
        comboquota.set(row[8])		



def disp():
    t.delete(*t.get_children())
    for row in db.fetch():
        t.insert("",END,values=row)

def addinfo():
        if txtname.get()=="" or txtage.get()=="" or txtdoa.get()=="" or txtsno.get()=="" or txtpno.get()=="" or combogender.get()=="" or empty()or comboquota.get()=="":
            messagebox.showerror("Alert","Please fill All the Info")
            return
        elif check():
            messagebox.showerror("Alert","Please Check the Details")
            return
        db.insert(txtname.get(),txtage.get(),combogender.get(),txtdoa.get(),txtsno.get(),txtpno.get(),txtad.get(1.0,END),comboquota.get())
        messagebox.showinfo("Sucess","Inserted Successfully")
        clear()
        disp()
    
def updateinfo():
        if txtname.get()=="" or txtage.get()=="" or txtdoa.get()=="" or txtsno.get()=="" or txtpno.get()=="" or combogender.get()=="" or empty() or comboquota.get()=="":
            messagebox.showerror("Alert","Please fill All the Info")
            return
        elif check():
            messagebox.showerror("Alert","Please Check the Details")
            return
        db.update(row[0],txtname.get(),txtage.get(),combogender.get(),txtdoa.get(),txtsno.get(),txtpno.get(),txtad.get(1.0,END),comboquota.get())
        messagebox.showinfo("Sucess","Record Updated")
        clear()
        disp()

def deleteinfo():
    if not(txtname.get()=="" or txtage.get()=="" or txtdoa.get()=="" or txtsno.get()=="" or txtpno.get()=="" or combogender.get()=="" or empty()or comboquota.get()==""):
            db.remove(row[0])
            messagebox.showinfo("Success","Removed Successfully")
            clear()
            disp()
    else:
            messagebox.showinfo("Alert !","Please Select To Delete")
def clear():
    name.set("")
    age.set("")
    doa.set("")
    gender.set("")
    quota.set("")
    sno.set("")
    pno.set("")
    txtad.delete(1.0,END)
    

def page2():
    f4.pack(side=TOP,fill=X)
    f6.pack(side=TOP,fill=X)
    f1.pack_forget()
    f3.pack_forget()
    f7.pack_forget()
    f8.pack_forget()
    disp1()
def page3():
    f7.pack(side=TOP,fill=X)
    f8.pack(side=TOP,fill=X)
    f1.pack_forget()
    f3.pack_forget()
    f4.pack_forget()
    f6.pack_forget()
    dispall()
def page1():
    f1.pack(side=TOP,fill=X)
    f3.pack(side=TOP,fill=X)
    f4.pack_forget()
    f6.pack_forget()
    f7.pack_forget()
    f8.pack_forget()
    disp()
def disp1():
    t1.delete(*t1.get_children())
    row1=db.fetch()
    row=db.fetch1()

    for row in db.fetch1():
            for row1 in db.fetch():
                    if row[0]==row1[0]:
                        t1.insert("",END,values=(row[0],row1[1],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

def getdata1(event):
    selectedrow=t1.focus()
    data=t1.item(selectedrow)
    global row1
    row1=data["values"]

    sid.set(row1[0])
    sem1.set(row1[2])
    sem2.set(row1[3])
    sem3.set(row1[4])
    sem4.set(row1[5])
    sem5.set(row1[6])
    sem6.set(row1[7])
    sem7.set(row1[8])
    sem8.set(row1[9])
def addinfo1():
        
        if sid.get()=="" or sem1.get()=="" or sem2.get()=="" or sem3.get()=="" or sem4.get()=="" or sem5.get()=="" or sem6.get()=="" or sem7.get()=="" or sem8.get()=="":
            messagebox.showerror("Alert","Please fill All the Info")
            return

        db.insert1(sid.get(),sem1.get(),sem2.get(),sem3.get(),sem4.get(),sem5.get(),sem6.get(),sem7.get(),sem8.get())
        messagebox.showinfo("Sucess","Inserted Successfully")
        clear1()
        disp1()

def updateinfo1():
        if sid.get()=="" or sem1.get()=="" or sem2.get()=="" or sem3.get()=="" or sem4.get()=="" or sem5.get()=="" or sem6.get()=="" or sem7.get()=="" or sem8.get()=="":
            messagebox.showerror("Alert","Please fill All the Info")
            return

        db.update1(row1[0],sem1.get(),sem2.get(),sem3.get(),sem4.get(),sem5.get(),sem6.get(),sem7.get(),sem8.get())
        messagebox.showinfo("Sucess","Record Updated")
        clear1()
        disp1()

def deleteinfo1():
    if not(sid.get()=="" or sem1.get()=="" or sem2.get()=="" or sem3.get()=="" or sem4.get()=="" or sem5.get()=="" or sem6.get()=="" or sem7.get()=="" or sem8.get()==""):
            db.remove1(row1[0])
            messagebox.showinfo("Success","Removed Successfully")
            clear1()
            disp1()
    else:
        messagebox.showinfo("Alert !","Please Select To Delete")
def clear1():
    sid.set("")
    sem1.set("0")
    sem2.set("0")
    sem3.set("0")
    sem4.set("0")
    sem5.set("0")
    sem6.set("0")
    sem7.set("0")
    sem8.set("0")
def search():
    if txtsearch.get()=="":
        messagebox.showerror("Alert","Enter Something")
        return
    for row in db.search(key.get()):
        for row1 in db.fetch1():
            if row[0]==row1[0] and row1[1]!="":
                t2.insert('',END,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row1[1],row1[2],row1[3],row1[4],row1[5],row1[6],row1[7],row1[8]))
            elif row1[1]=="":
                t2.insert('',END,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],0,0,0,0,0,0,0,0))
def clrtbl():
    for i in t2.get_children():
        t2.delete(i)
def dispall():
    clrtbl()
    for row in db.fetch():
        for row1 in db.fetch1():
            if row[0]==row1[0] and row1[1]!="":
                t2.insert('',END,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row1[1],row1[2],row1[3],row1[4],row1[5],row1[6],row1[7],row1[8]))
            elif row1[1]=="":
                t2.insert('',END,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],0,0,0,0,0,0,0,0))
#window
root=Tk()
root.title("Students Details")
root.geometry("1920x1080")
root.config(bg="#ff0000")
root.state("zoomed")

name=StringVar()
age=StringVar()
doa=StringVar()
gender=StringVar()
doa=StringVar()
sno=StringVar()
pno=StringVar()
address=StringVar()
quota=StringVar()
#frme
f=Frame(root,bg="#800040")
f.pack(side=TOP)

#menubutton
btnhome=Button(f,command=page1,text="Home",width=15,font=("Tahoma",16,"bold"),bg="#2980b9",fg="white",bd=0).grid(row=0,column=0,sticky='w')
btnfilter=Button(f,command=page2,text="Semester",width=15,font=("Tahoma",16,"bold"),bg="#2980b9",fg="white",bd=0).grid(row=0,column=1,sticky='w')
btnsemseter=Button(f,command=page3,text="Search",width=15,font=("Tahoma",16,"bold"),bg="#2980b9",fg="white",bd=0).grid(row=0,column=2,sticky='w')

#page1-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#frame1
f1=Frame(root,bg="#ffcccc")
f1.pack(side=TOP,fill=X)
#title
title=Label(f1,text="Students Details",font=("Tahoma",18,"bold"),bg="#ffcccc",fg="black")
title.grid(row=0,columnspan=2,padx=10,pady=20,sticky="w")
#name
lbn=Label(f1,text="Name",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbn.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtname=Entry(f1,textvariable=name,font=("Tahoma",16),width=30)
txtname.grid(row=1,column=1,padx=10,pady=10,sticky="w")
#age
lbage=Label(f1,text="Age",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbage.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtage=Entry(f1,textvariable=age,font=("Tahoma",16),width=30)
txtage.grid(row=1,column=3,padx=10,pady=10,sticky="w")
#doa
lbdoa=Label(f1,text="Date Of Admission\n(DD/MM/YYYY)",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbdoa.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtdoa=Entry(f1,textvariable=doa,font=("Tahoma",16),width=30)
txtdoa.grid(row=2,column=1,padx=10,pady=10,sticky="w")
#gender
lbgender=Label(f1,text="Gender",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbgender.grid(row=2,column=2,padx=10,pady=10,sticky="w")
combogender=ttk.Combobox(f1,textvariable=gender,font=("Tahoma",16),width=28,state="readonly")
combogender["values"]=("Male","Female")
combogender.grid(row=2,column=3,padx=10,pady=10,sticky="w")
#sno
lbsno=Label(f1,text="Student Phno.",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbsno.grid(row=3,column=0,padx=10,pady=10,sticky="w")
txtsno=Entry(f1,textvariable=sno,font=("Tahoma",16),width=30)
txtsno.grid(row=3,column=1,padx=10,pady=10,sticky="w")
#phno
lbpno=Label(f1,text="Parent Phno.",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbpno.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txtpno=Entry(f1,textvariable=pno,font=("Tahoma",16),width=30)
txtpno.grid(row=3,column=3,padx=10,pady=10,sticky="w")
#quota
lbquota=Label(f1,text="quota",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbquota.grid(row=4,column=2,padx=10,pady=10,sticky="w")
comboquota=ttk.Combobox(f1,textvariable=quota,font=("Tahoma",16),width=28,state="readonly")
comboquota["values"]=("GQ","MQ")
comboquota.grid(row=4,column=3,padx=10,pady=10,sticky="w")
#address
lbad=Label(f1,text="Address",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbad.grid(row=4,column=0,padx=10,pady=10,sticky="w")
txtad=Text(f1,height=5,width=30,font=("Tahoma",16))
txtad.grid(row=4,column=1,columnspan=4,padx=10,pady=10,sticky="w")
#buttonframe
f2=Frame(f1,bg="#ffcccc")
f2.grid(row=5,column=1,columnspan=4,padx=10,pady=10,sticky="w")
btnadd=Button(f2,command=addinfo,text="Add Info",width=15,font=("Tahoma",16,"bold"),bg="#16a085",fg="white",bd=0).grid(row=0,column=0,padx=10)
btnupdate=Button(f2,command=updateinfo,text="Update Info",width=15,font=("Tahoma",16,"bold"),bg="#2980b9",fg="white",bd=0).grid(row=0,column=1,padx=10)
btndel=Button(f2,command=deleteinfo,text="Delete Info",width=15,font=("Tahoma",16,"bold"),bg="#c0392b",fg="white",bd=0).grid(row=0,column=2,padx=10)
btnclear=Button(f2,command=clear,text="Clear Info",width=15,font=("Tahoma",16,"bold"),bg="#f39c12",fg="white",bd=0).grid(row=0,column=3,padx=10)
#frame3
f3=Frame(root,bg="White",height=10)
f3.pack(side=TOP,fill=X)
style=ttk.Style()
style.configure("mystyle.Treeview",font=("Tahoma",16),rowheight=60)
style.configure("mystyle.Treeview.Heading",font=("Tahoma",18,'bold'))
sb=Scrollbar(f3)
sb.pack(side=RIGHT,fill=Y)
#table
t=ttk.Treeview(f3,columns=(1,2,3,4,5,6,7,8,9),style="mystyle.Treeview",yscrollcommand=sb.set)
sb.config(command=t.yview)
t.heading("1",text="ID")
t.column('1',width=5)
t.heading("2",text="Name")
t.column('2',width=20)
t.heading("3",text="Age")
t.column('3',width=5)
t.heading("4",text="Gender")
t.column('4',width=8)
t.heading("5",text="DOA")
t.column('5',width=25)
t.heading("6",text="Student Phno.")
t.column('6',width=25)
t.heading("7",text="Parent Phno.")
t.column('7',width=20)
t.heading("8",text="Address")
t.column('8',width=25)
t.heading("9",text="Quota")
t.column('9',width=5)
t['show']='headings'
t.bind("<ButtonRelease-1>",getdata)
t.pack(fill=X)

disp()
#page2-------------------------------------------------------------------------------------------------------------------------------------------------------------------
f4=Frame(root,bg="#ffcccc")
f4.pack(side=TOP,fill=X)

title=Label(f4,text="Semester",font=("Tahoma",18,"bold"),bg="#ffcccc",fg="black")
title.grid(row=0,columnspan=2,padx=10,pady=20,sticky="w")
sid=StringVar()

lbi=Label(f4,text="Student ID",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbi.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtid=Entry(f4,textvariable=sid,font=("Tahoma",16),width=30)
txtid.grid(row=1,column=1,padx=10,pady=10,sticky="w")

sem1=StringVar()
sem2=StringVar()
sem3=StringVar()
sem4=StringVar()
sem5=StringVar()
sem6=StringVar()
sem7=StringVar()
sem8=StringVar()

lbsem1=Label(f4,text="Semester 1",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbsem1.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtsem1=Entry(f4,textvariable=sem1,font=("Tahoma",16),width=30)
txtsem1.grid(row=2,column=1,padx=10,pady=10,sticky="w")
txtsem1.insert(END,'0')

lbsem2=Label(f4,text="Semester 2",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbsem2.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txtsem2=Entry(f4,textvariable=sem2,font=("Tahoma",16),width=30)
txtsem2.grid(row=2,column=3,padx=10,pady=10,sticky="w")
txtsem2.insert(END,'0')

lbsem3=Label(f4,text="Semester 3",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbsem3.grid(row=3,column=0,padx=10,pady=10,sticky="w")
txtsem3=Entry(f4,textvariable=sem3,font=("Tahoma",16),width=30)
txtsem3.grid(row=3,column=1,padx=10,pady=10,sticky="w")
txtsem3.insert(END,'0')

lbsem4=Label(f4,text="Semester 4",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbsem4.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txtsem4=Entry(f4,textvariable=sem4,font=("Tahoma",16),width=30)
txtsem4.grid(row=3,column=3,padx=10,pady=10,sticky="w")
txtsem4.insert(END,'0')

lbsem5=Label(f4,text="Semester 5",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbsem5.grid(row=4,column=0,padx=10,pady=10,sticky="w")
txtsem5=Entry(f4,textvariable=sem5,font=("Tahoma",16),width=30)
txtsem5.grid(row=4,column=1,padx=10,pady=10,sticky="w")
txtsem5.insert(END,'0')

lbsem6=Label(f4,text="Semester 6",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbsem6.grid(row=4,column=2,padx=10,pady=10,sticky="w")
txtsem6=Entry(f4,textvariable=sem6,font=("Tahoma",16),width=30)
txtsem6.grid(row=4,column=3,padx=10,pady=10,sticky="w")
txtsem6.insert(END,'0')

lbsem7=Label(f4,text="Semester 7",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbsem7.grid(row=5,column=0,padx=10,pady=10,sticky="w")
txtsem7=Entry(f4,textvariable=sem7,font=("Tahoma",16),width=30)
txtsem7.grid(row=5,column=1,padx=10,pady=10,sticky="w")
txtsem7.insert(END,'0')

lbsem8=Label(f4,text="Semester 8",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbsem8.grid(row=5,column=2,padx=10,pady=10,sticky="w")
txtsem8=Entry(f4,textvariable=sem8,font=("Tahoma",16),width=30)
txtsem8.grid(row=5,column=3,padx=10,pady=10,sticky="w")
txtsem8.insert(END,'0')

f5=Frame(f4,bg="#ffcccc")
f5.grid(row=6,column=1,columnspan=4,padx=10,pady=10,sticky="w")
btnadd=Button(f5,command=addinfo1,text="Add Info",width=15,font=("Tahoma",16,"bold"),bg="#16a085",fg="white",bd=0).grid(row=0,column=0,padx=10)
btnupdate=Button(f5,command=updateinfo1,text="Update Info",width=15,font=("Tahoma",16,"bold"),bg="#2980b9",fg="white",bd=0).grid(row=0,column=1,padx=10)
btndel=Button(f5,command=deleteinfo1,text="Delete Info",width=15,font=("Tahoma",16,"bold"),bg="#c0392b",fg="white",bd=0).grid(row=0,column=2,padx=10)
btnclear=Button(f5,command=clear1,text="Clear Info",width=15,font=("Tahoma",16,"bold"),bg="#f39c12",fg="white",bd=0).grid(row=0,column=3,padx=10)

f6=Frame(root,bg="White",height=10)
f6.pack(side=TOP,fill=X)

sb1=Scrollbar(f6)
sb1.pack(side=RIGHT,fill=Y)
#table
t1=ttk.Treeview(f6,columns=(1,2,3,4,5,6,7,8,9,10),style="mystyle.Treeview",yscrollcommand=sb1.set)
sb1.config(command=t.yview)
t1.heading("1",text="ID")
t1.column('1',width=5,anchor="center")
t1.heading("2",text="Name")
t1.column('2',width=15,anchor="center")
t1.heading("3",text="Sem 1")
t1.column('3',width=10,anchor="center")
t1.heading("4",text="Sem 2")
t1.column('4',width=10,anchor="center")
t1.heading("5",text="Sem 3")
t1.column('5',width=10,anchor="center")
t1.heading("6",text="Sem 4")
t1.column('6',width=10,anchor="center")
t1.heading("7",text="Sem 5")
t1.column('7',width=10,anchor="center")
t1.heading("8",text="Sem 6")
t1.column('8',width=10,anchor="center")
t1.heading("9",text="Sem 7")
t1.column('9',width=10,anchor="center")
t1.heading("10",text="Sem 8")
t1.column('10',width=10,anchor="center")
t1['show']='headings'
t1.bind("<ButtonRelease-1>",getdata1)
t1.pack(fill=X)
disp1()
#page3--------------------------------------------------------------------------------------------------------------------------------------------------------------------
key=StringVar()
f7=Frame(root,bg="#ffcccc")
f7.pack(side=TOP,fill=X)

title=Label(f7,text="Search",font=("Tahoma",18,"bold"),bg="#ffcccc",fg="black")
title.grid(row=0,columnspan=2,padx=10,pady=20,sticky="w")

lbsearch=Label(f7,text="Search By Word/ID",font=("Tahoma",16),bg="#ffcccc",fg="black")
lbsearch.grid(row=1,column=0,padx=10,pady=10,sticky="w")

txtsearch=Entry(f7,textvariable=key,font=("Tahoma",16),width=30)
txtsearch.grid(row=2,column=0,padx=10,pady=10,sticky="w")

btnsearch=Button(f7,command=search,text="Find",width=15,font=("Tahoma",16,"bold"),bg="#c0392b",fg="white",bd=0).grid(row=2,column=1,sticky='w')

btnclrtbl=Button(f7,command=clrtbl,text="Clear Table",width=15,font=("Tahoma",16,"bold"),bg="#f39c12",fg="white",bd=0).grid(row=2,column=2,sticky='w',padx=10)

btndispall=Button(f7,command=dispall,text="Display All",width=15,font=("Tahoma",16,"bold"),bg="#16a085",fg="white",bd=0).grid(row=2,column=3,sticky='w',padx=10)



f8=Frame(root,bg="White")
f8.pack(side=TOP,fill=X)
style=ttk.Style()
style.configure("mystyle.Treeview",font=("Tahoma",16),rowheight=60)
style.configure("mystyle.Treeview.Heading",font=("Tahoma",18,'bold'))
sb2=Scrollbar(f8)
sb2.pack(side=RIGHT,fill=Y)
sb3=Scrollbar(f8,orient='horizontal')
sb3.pack(side=BOTTOM,fill=X)
t2=ttk.Treeview(f8,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17),style="mystyle.Treeview",yscrollcommand=sb2.set,xscrollcommand=sb3.set)
sb2.config(command=t2.yview)
sb3.config(command=t2.xview)
t2.heading("1",text="ID")

t2.heading("2",text="Name")

t2.heading("3",text="Age")

t2.heading("4",text="Gender")

t2.heading("5",text="DOA")

t2.heading("6",text="Student Phno.")

t2.heading("7",text="Parent Phno.")

t2.heading("8",text="Address")

t2.heading("9",text="Quota")

t2.heading("10",text="Sem 1")

t2.heading("11",text="Sem 2")

t2.heading("12",text="Sem 3")

t2.heading("13",text="Sem 4")

t2.heading("14",text="Sem 5")

t2.heading("15",text="Sem 6")

t2.heading("16",text="Sem 7")

t2.heading("17",text="Sem 8")
t2.bind("<ButtonRelease-1>",generatepdf)
t2['show']='headings'
t2.pack(fill=X)
dispall()
root.mainloop()
