from tkinter import *
import time
import sqlite3
from tkinter import messagebox
try:
    conobj=sqlite3.connect(database='bank.sqlite')
    curobj=conobj.cursor()
    curobj.execute("""create table acn
                   (acn_acno integer primary key autoincrement,
                   acn_name text,acn_pass text,acn_email text,
                   acn_mob text,acn_bal float,acn_opendate text)""")
    print('Table Created...')
except:
    print('table already exists or there is some error')
conobj.close()
win=Tk()
win.configure(bg='powder blue')
win.state('zoomed')
win.resizable(width=False,height=False)
t1=Label(win,text='Banking Automation System',
         font=('arial',45,'bold','underline'),bg='powder blue')
t1.pack()
date=time.strftime('%d-%m-%Y')
t2=Label(win,text=date,font=('arial',20,'bold'),bg='powder blue')
t2.place(relx=.87,rely=.1)
def newscreen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    def newacn():
        name=e_name.get()
        pwd=e_pass.get()
        email=e_email.get()
        mob=e_mob.get()
        bal=0
        date=time.strftime('%d-%m-%Y')
        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute("""insert into acn(acn_name,acn_pass,acn_email,acn_mob,
acn_opendate,acn_bal) values(?,?,?,?,?,?)""",(name,pwd,email,mob,date,bal))
        conobj.commit()
        conobj.close()
        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute("select max(acn_acno) from acn")
        tup=curobj.fetchone()
        conobj.close()
        messagebox.showinfo('New Account',f'Account Created,ACN:{tup[0]}')
    

    lbl_name=Label(frm,text='Name',
                  font=('arial',20,'bold'),bg='pink')
    lbl_name.place(relx=.3,rely=.1)

    e_name=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_name.focus()
    e_name.place(relx=.4,rely=.1)

    lbl_pass=Label(frm,text='Pass',
                  font=('arial',20,'bold'),bg='pink')
    lbl_pass.place(relx=.3,rely=.2)

    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    e_pass.place(relx=.4,rely=.2)

    lbl_email=Label(frm,text='Email',
                  font=('arial',20,'bold'),bg='pink')
    lbl_email.place(relx=.3,rely=.3)

    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.4,rely=.3)

    lbl_mob=Label(frm,text='Mob',
                  font=('arial',20,'bold'),bg='pink')
    lbl_mob.place(relx=.3,rely=.4)

    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=.4,rely=.4)

    btn_submit=Button(frm,text='Submit',command=newacn,font=('arial',20,'bold'),bd=5)
    btn_submit.place(relx=.45,rely=.6)

    
    def back():
        frm.destroy()
        mainscreen()
        
    btn_back=Button(frm,command=back,text='back',font=('arial',20,'bold'),bd=5)
    btn_back.place(relx=0,rely=0)
def loginscreen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    conobj=sqlite3.connect(database='bank.sqlite')
    curobj=conobj.cursor()
    curobj.execute("""select * from acn where acn_acno=?""",(acn,))
    tup=curobj.fetchone()
    conobj.close()
    
    frm=Frame(win)
    frm.configure(bg='beige')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    l1=Label(frm,text=f'Welcome,{tup[1]}',
                 font=('arial',20,'bold'),bg='beige')
    l1.place(relx=0,rely=0)
    
    def logout():
        frm.destroy()
        mainscreen()
    backbtn=Button(frm,command=logout,text='logout',font=('arial',18,'bold'))
    backbtn.place(relx=.925,rely=0)

    def checkdet():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.15,relwidth=.7,relheight=.6)
        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute("select * from acn where acn_acno=?",(acn,))
        tup=curobj.fetchone()
        conobj.close()
        lbl_wel=Label(ifrm,text='This is Details Screen',
                  font=('arial',20,'bold'),bg='white',fg='purple')
        lbl_wel.pack()
        lbl_acn=Label(ifrm,text=f'Account no={tup[0]}',
                  font=('arial',20,'bold'),bg='white')
        lbl_acn.place(relx=.3,rely=.2)

        lbl_bal=Label(ifrm,text=f'Your Acn Bal={tup[5]}',
                  font=('arial',20,'bold'),bg='white')
        lbl_bal.place(relx=.3,rely=.3)

        lbl_date=Label(ifrm,text=f'Acn opendate={tup[6]}',
                  font=('arial',20,'bold'),bg='white')
        lbl_date.place(relx=.3,rely=.4)
    

    def depamt():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.15,relwidth=.7,relheight=.6)
        def depacn():
            amt=e_amt.get()
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute("""update acn set acn_bal=acn_bal+? where
                           acn_acno=?""",(amt,acn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo('Deposited',f'{amt} deposited successfully...')
        lbl_wel=Label(ifrm,text='This is Deposit Screen',
                  font=('arial',20,'bold'),bg='white',fg='purple')
        lbl_wel.pack()
        lbl_amt=Label(ifrm,text='Amount',
                  font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=.2,rely=.2)

        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.35,rely=.2)

        btn_submit=Button(ifrm,text='Submit',command=depacn,font=('arial',20,'bold'),bd=5)
        btn_submit.place(relx=.4,rely=.35)

    def withamt():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.15,relwidth=.7,relheight=.6)
        def witacn():
            amt=e_amt.get()
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute("""update acn set acn_bal=acn_bal-? where
                           acn_acno=?""",(amt,acn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo('Deducted',f'{amt} deducted successfully...')

    
        lbl_wel=Label(ifrm,text='This is Withdrawl Screen',
                  font=('arial',20,'bold'),bg='white',fg='purple')
        lbl_wel.pack()
        lbl_amt=Label(ifrm,text='Amount',
                  font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=.2,rely=.2)

        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.35,rely=.2)

        btn_submit=Button(ifrm,text='Submit',command=witacn,font=('arial',20,'bold'),bd=5)
        btn_submit.place(relx=.4,rely=.35)

    def updet():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.15,relwidth=.7,relheight=.6)

        def updateacc():
            name=e_name.get()
            pwd=e_pass.get()
            email=e_email.get()
            mob=e_mob.get()
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute("""update acn set acn_name=?,acn_pass=?
            ,acn_mob=?,acn_email=? where acn_acno=?""",
                           (name,pwd,mob,email,acn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo('Updated','info updated successfully...')
            frm.destroy()
            loginscreen()
        
        lbl_wel=Label(ifrm,text='This is Update Screen',
                  font=('arial',20,'bold'),bg='white',fg='purple')
        lbl_wel.pack()
        lbl_name=Label(ifrm,text='Name',font=('arial',20,'bold'),bg='white')
        lbl_name.place(relx=.1,rely=.2)
        e_name=Entry(ifrm,bd=5,font=('arial',20,'bold'))
        e_name.place(relx=.1,rely=.3)
        lbl_pass=Label(ifrm,text='Pass',font=('arial',20,'bold'),bg='white')
        lbl_pass.place(relx=.1,rely=.45)
        e_pass=Entry(ifrm,bd=5,font=('arial',20,'bold'))
        e_pass.place(relx=.1,rely=.55)
        lbl_email=Label(ifrm,text='Email',font=('arial',20,'bold'),bg='white')
        lbl_email.place(relx=.6,rely=.2)
        e_email=Entry(ifrm,bd=5,font=('arial',20,'bold'))
        e_email.place(relx=.6,rely=.3)
        lbl_mob=Label(ifrm,text='MOB',font=('arial',20,'bold'),bg='white')
        lbl_mob.place(relx=.6,rely=.45)
        e_mob=Entry(ifrm,bd=5,font=('arial',20,'bold'))
        e_mob.place(relx=.6,rely=.55)
        btn_update=Button(frm,text='Update',command=updateacc,width=12,font=('arial',20,'bold'),bd=5)
        btn_update.place(relx=.47,rely=.58)
        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute("select * from acn where acn_acno=?",(acn,))
        tup=curobj.fetchone()
        conobj.close()
        e_name.insert(0,tup[1])
        e_pass.insert(0,tup[2])
        e_email.insert(0,tup[3])
        e_mob.insert(0,tup[4])
        e_name.focus()
        
    b1=Button(frm,text='check details',command=checkdet,width=12,font=('arial',20,'bold'),bd=5)
    b1.place(relx=0,rely=.23)
    b2=Button(frm,text='deposit amt',command=depamt,width=12,font=('arial',20,'bold'),bd=5)
    b2.place(relx=0,rely=.33)
    b3=Button(frm,text='withdraw amt',command=withamt,width=12,font=('arial',20,'bold'),bd=5)
    b3.place(relx=0,rely=.43)
    b4=Button(frm,text='update details',command=updet,width=12,font=('arial',20,'bold'),bd=5)
    b4.place(relx=0,rely=.53)
    
def fgtscreen():
    frm=Frame(win)
    frm.configure(bg='lavender')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    def back():
        frm.destroy()
        mainscreen()
    backbtn=Button(frm,command=back,text='back',font=('arial',18,'bold'))
    backbtn.place(relx=0,rely=0)
    t5=Label(frm,text='EMAIL',font=('arial',20,'bold'),bg='lavender')
    t5.place(relx=.35,rely=.25)
    e3=Entry(frm,bd=5,font=('arial',20,'bold'))
    e3.place(relx=.45,rely=.25)
    e3.focus()
    t6=Label(frm,text='MOB',font=('arial',20,'bold'),bg='lavender')
    t6.place(relx=.35,rely=.35)
    e4=Entry(frm,bd=5,font=('arial',20,'bold'))
    e4.place(relx=.45,rely=.35)
    t7=Label(frm,text='ACN',font=('arial',20,'bold'),bg='lavender')
    t7.place(relx=.35,rely=.45)
    e5=Entry(frm,bd=5,font=('arial',20,'bold'))
    e5.place(relx=.45,rely=.45)
    def subdet():
        email=e3.get()
        mob=e4.get()
        acn=e5.get()
        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute("""select * from acn where acn_acno=? and
                        acn_email=? and acn_mob=?""",(acn,email,mob))
        tup=curobj.fetchone()
        conobj.close()
        if tup==None:
            messagebox.showwarning('Warning','Incorrect Details!')
        else:
            messagebox.showinfo('Password',f'Your password is {tup[2]}')
        frm.destroy()
        mainscreen()
        
    b1=Button(frm,text='submit',command=subdet,font=('arial',20,'bold'))
    b1.place(relx=.4,rely=.6)
    
def mainscreen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    t3=Label(frm,text='ACN',font=('arial',20,'bold'),bg='pink')
    t3.place(relx=.3,rely=.15)
    e1=Entry(frm,bd=5,font=('arial',20,'bold'))
    e1.focus()
    e1.place(relx=.4,rely=.15)
    t4=Label(frm,text='PASS',font=('arial',20,'bold'),bg='pink')
    t4.place(relx=.3,rely=.25)
    e2=Entry(frm,bd=5,font=('arial',20,'bold'),show='*')
    e2.place(relx=.4,rely=.25)

    def login():
        global acn
        acn=e1.get()
        pwd=e2.get()
        if len(acn)==0 or len(pwd)==0:
            messagebox.showwarning('validation','Empty fields are not allowed')
        else:
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute("""select * from acn where acn_acno=? and
            acn_pass=?""",(acn,pwd))
            tup=curobj.fetchone()
            if tup==None:
                messagebox.showerror('Validation','No record found!')
            else:            
                frm.destroy()
                loginscreen()
    
    b1=Button(frm,text='login',command=login,font=('arial',18,'bold'))
    b1.place(relx=.43,rely=.42)
    
    def reset():
        frm.destroy()
        mainscreen()
        
    b2=Button(frm,text='reset',command=reset,font=('arial',18,'bold'))
    b2.place(relx=.53,rely=.42)

    def fgtpass():
        frm.destroy()
        fgtscreen()
    
    b3=Button(frm,text='forgot password',command=fgtpass,font=('arial',18,'bold'))
    b3.place(relx=.43,rely=.52)

    def newyscreen():
        frm.destroy()
        newscreen()
        
    b4=Button(frm,text='new user',command=newyscreen,font=('arial',18,'bold'))
    b4.place(relx=.46,rely=.62)


mainscreen()
win.mainloop()
