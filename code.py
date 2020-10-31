from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="shivam2667",database="kk1")
cursor=con.cursor()
 
#cursor.execute("create database kk1")
#cursor.execute("create table kk1 (First_name varchar(22),Last_name varchar(22),Mobile int(30))")
rahul=Tk()
rahul.title("BUS RESERVATION SYSTEM")
rahul.geometry("1100x1200")
c=Canvas(rahul,height=1000,width=1500)
p=Image.open("C:/Users/shubham/Desktop/BUS.png")
f=ImageTk.PhotoImage(p)
c.create_image(600,350,image=f)
Label(rahul,text="WELCOME ON LOGIN PAGE",font=("Courier",30,"italic","bold"),fg="red",bg="green").place(x=450,y=50)
rahul.configure(bg='orange')
username=StringVar()
password=StringVar()
Label(c,text="User Name",fg="white",bg="black",width=30).place(x=400,y=200)
Label(c,text="Password",fg="white",bg="black",width=30).place(x=400,y=250)
a=Entry(c,textvariable=username,bg="orange",width=60)
a.place(x=650,y=200)
b=Entry(c,textvariable=password,bg="orange",width=60,show="*")
b.place(x=650,y=250)
c.pack()
def login():
    if username.get()=="LPU" and password.get()=="12345":
        messagebox.showinfo("successful","Welcome in best Bus service")
        root=Tk()
        def new():
            x=Tk()
            x.mainloop()
        a=Menu(root)
        file=Menu(a)
        a.add_cascade(label="File",menu=file)
        file.add_command(label="New",command=new)
        file.add_command(label="Make Copy")
        file.add_separator()
        file.add_command(label="Open ")
        file.add_command(label="Exit",command=root.destroy)
        root.config(menu=a)
        root.configure(bg="gold")
        def BOOK():
            z=Tk()
            z.title("BOOK YOUR TICKET")
            z.configure(bg="pink")
            Label(z,text="Select your journey Status:",fg="black",bg="purple",font=("Courier",15,"italic","bold")).grid(row=1)
            Label(z,text="From",fg="black",font=("Courier",15,"italic","bold")).grid(row=2,column=1)
            Entry(z,bg="red",fg="indigo",font=("Courier",15,"italic")).grid(row=2,column=2)
            Label(z,text="=======>  To",fg="black",font=("Courier",15,"italic","bold")).grid(row=2,column=3)
            Entry(z,bg="red",fg="indigo",font=("Courier",15,"italic")).grid(row=2,column=4)
            Label(z,text="Select date:",fg="black",font=("Courier",15,"italic","bold")).grid(row=3)
            Label(z,text="Date:",fg="black",font=("Courier",10,"italic","bold")).grid(row=4,column=1)
            Spinbox(z,from_=1,to=31).grid(row=4,column=2)

            Label(z,text="Month:",fg="black",font=("Courier",10,"italic","bold")).grid(row=4,column=3)
            Spinbox(z,from_=1,to=12).grid(row=4,column=4)
            Label(z,text="Year:",fg="black",font=("Courier",10,"italic","bold")).grid(row=4,column=5)
            Spinbox(z,from_=2020,to=2025).grid(row=4,column=6)
            
            
        
            def search():
                A=Tk()
                A.configure(bg="violet")
                Label(A,text="Details of Bus at this day",fg="green",bg="violet",font=("Courier",15,"italic","bold")).grid(row=1)
                Label(A,text="   Bus Name            Time         Price",fg="brown",bg="violet",font=("Courier",15,"italic","bold")).grid(row=2)
                Label(A,text="VRL Travels           7:00 AM       100", fg="blue",bg="violet",font=("Courier",15,"italic","bold")).grid(row=3)
                Label(A,text="SRS Travels           8:20 PM       70",fg="blue",bg="violet",font=("Courier",15,"italic","bold")).grid(row=4)
                Label(A,text="SRM Travels           3:00 PM       85",fg="blue",bg="violet",font=("Courier",15,"italic","bold")).grid(row=5)
                Label(A,text="Quantity of Ticket :",fg="white",bg="gray",font=("Courier",15,"italic","bold")).place(x=20,y=150)
                Spinbox(A,from_=1,to=31).place(x=270,y=155)
                Label(A,text="Aget :",fg="white",bg="gray",font=("Courier",15,"italic","bold")).place(x=20,y=195)
                Spinbox(A,from_=1,to=100).place(x=100,y=200)
                
                Label(A,text="choose your bus",font=("Courier",20,"italic","bold"),fg="black",bg="orange",width=35).place(x=350,y=200)           
                Label(A,text="VRL",font=("Courier",20,"italic","bold"),fg="white",bg="indigo",width=20).place(x=450,y=250)           
                Label(A,text="SRS",font=("Courier",20,"italic","bold"),fg="white",bg="green",width=20).place(x=450,y=300)          
                Label(A,text="SRM",font=("Courier",20,"italic","bold"),fg="white",bg="red",width=20).place(x=450,y=350)           
                Radiobutton(A,value=1,bg="violet").place(x=900,y=250)
                Radiobutton(A,value=2,bg="violet").place(x=900,y=300)
                Radiobutton(A,value=3,bg="violet").place(x=900,y=350)
                Button(A,text="OK",bg="black",fg="white",font=("Courier",20,"italic","bold"),activebackground="yellow",width=35,command=A.destroy).place(x=350,y=400)  
                A.mainloop()
            def payment():
                d=Tk()
                d.title("Payment Method")
                d.configure(bg='pink')
                Label(d,text="PAY BALANCE",font=("Courier",40,"italic","bold"),fg="gray",bg="purple",width=25).place(x=450,y=50)
               
                Label(d,text="Debit Card",font=("Courier",20,"italic","bold"),fg="black",bg="orange",width=35).place(x=500,y=200)         
                Label(d,text="PAYTM",font=("Courier",20,"italic","bold"),fg="black",bg="orange",width=35).place(x=500,y=300)         
                Label(d,text="BHIM UPI",font=("Courier",20,"italic","bold"),fg="black",bg="orange",width=35).place(x=500,y=400)         
                Label(d,text="Net Banking",font=("Courier",20,"italic","bold"),fg="black",bg="orange",width=35).place(x=500,y=500)   
                
                Radiobutton(d,value=1,bg="pink").place(x=1100,y=205)
                Radiobutton(d,value=2,bg="pink").place(x=1100,y=305)
                Radiobutton(d,value=3,bg="pink").place(x=1100,y=405)
                Radiobutton(d,value=4,bg="pink").place(x=1100,y=505)
                def pay():
                    z1=Tk()
                    z1.configure(bg="purple")
                    Label(z1,text="Available balance in your account : 10,000 ",font=("Courier",20,"italic","bold"),fg="gray",bg="yellow",width=45).place(x=450,y=50)
                    Label(z1,text="Card Number ",font=("Courier",20,"italic","bold"),fg="gray",bg="yellow",width=20).place(x=450,y=200)
                    Label(z1,text="CVV",font=("Courier",20,"italic","bold"),fg="gray",bg="yellow",width=20).place(x=450,y=300)
                    Label(z1,text="Expiary Date ",font=("Courier",20,"italic","bold"),fg="gray",bg="yellow",width=20).place(x=450,y=400)
                    Label(z1,text="Enter your amount",font=("Courier",20,"italic","bold"),fg="gray",bg="yellow",width=20).place(x=450,y=500)
                    Entry(z1,bg="pink", width=40).place(x=800,y=205)
                    Entry(z1,bg="pink", width=40).place(x=800,y=305)
                    Entry(z1,bg="pink", width=40).place(x=800,y=405)
                    Entry(z1,bg="pink", width=40).place(x=800,y=505)
                    
                    def maddy():
                        messagebox.showinfo("this is message","Payment Successfull")
                    Button(z1,text="Done",fg="black",bg="orange",font=("Courier",20,"italic"),width=18,command=maddy).place(x=600,y=605)
                    z1.mainloop()
                Button(d,text="PAY",bg="green",fg="black",activebackground="blue",font=("Courier",20,"italic","bold"), width=22,command=pay).place(x=630,y=600)
                d.mainloop()                
            Button(z,text="Search your Bus",fg="white",bg="blue",font=("Courier",16,"italic","bold"),width=18,command=search).grid(row=12,column=3)
            Button(z,text="Payment",fg="brown",bg="green",font=("Courier",16,"italic","bold"),width=18,command=payment).grid(row=14,column=3)
            Button(z,text="OK",bg="orange",fg="black",activebackground="blue",font=("Courier",16,"italic","bold"),width=18,command=z.destroy).grid(row=16,column=3)
            z.mainloop()
            ###########################
        def help():
            c=Tk()
            c.configure(bg="orange")
            c.geometry("1000x250")
            Label(c,text="For any query go on this link:",fg="blue",font=("Courier",15,"italic","bold")).grid(row=1,column=0)
            Label(c,text="https://www.youtube.com/channel/Techno Geek.com",fg="red",font=("Courier",15,"underline")).grid(row=2,column=3)
            Label(c,text="contact us:",fg="blue",font=("Courier",15,"italic","bold")).grid(row=3,column=0)
            Label(c,text="+91 9555607083",fg="red",font=("Courier",15,"underline")).grid(row=4,column=3)
            Label(c,text="Type your query",fg="purple",bg="green",font=("Courier",20,"bold"),width=18).grid(row=7,column=3)
            text=Text(c)
            text.grid(row=8,column=3)
            Button(c,text="Submit",fg="orange",bg="black",font=("Courier",20,"italic","bold"),width=18,command=c.destroy).grid(row=9,column=3)
            c.mainloop()
            ############################
        def about():
            d=Tk()
            d.configure(bg="orange")
            text=Text(d)
            text.insert(INSERT,"This is a very fantastic Bus resrvation ticket service .There are lot of features are there in this app.This app is itroduced by a Lpu student in 2020.This app is friendly for everyone This is devolped with the help of a indian IT company.\n \n A huge number of users are usingit now a days.There are so many advatages of this app.you can book your ticket from your home and enjoy your journey.The main thing is there in this app is the security  no one can hack it.\n \n There are so many functions are there in this app.The number of users is become increase day by day in 2020 there are only 10000 users were there but now a days it become 1 corore.")
            text.pack()
            d.mainloop()
            ###########################
        def Feedback():
            w=Tk()
            w.configure(bg="green")
            Label(w,text="CUSTOMER FEEDBACK",font=("Courier",30,"italic","bold"),fg="white",width=18,bg="black").place(x=450,y=40)
            Label(w,text="PLEASE TELL US WHAT DO YOU THINK",font=("Courier",20,"italic","bold"),fg="white",bg="GREEN").place(x=430,y=100)
            Label(w,text="Name",fg="white",bg="black",width=30).place(x=450,y=150)
            Label(w,text="Email",fg="white",bg="black",width=30).place(x=450,y=200)
            a=Entry(w, bg="orange",width=60)
            a.place(x=750,y=150)
            b=Entry(w ,bg="orange",width=60)
            b.place(x=750,y=200)
            Label(w,text="Comment",fg="black",bg="green",font=("Courier",20,"italic","bold")).place(x=450,y=220)
            text=Text(w)
            text.place(x=450,y=250)
            Button(w,text="Done",fg="white",bg="purple",font=("Courier",20,"italic"),width=18,command=w.destroy).place(x=610,y=640)
            w.mainloop()
        Button(root,text="BOOK Your Ticket",fg="white",bg="black",font=("Courier",15,"italic"),command=BOOK).grid(row=1)
        Button(root,text="Help",fg="white",bg="black",font=("Courier",15,"italic"),command=help).grid(row=1,column=1)
        Button(root,text="About app",fg="white",bg="black",font=("Courier",15,"italic"),command=about).grid(row=1,column=2)
        Button(root,text="Feedback",fg="white",bg="black",font=("Courier",15,"italic"),command=Feedback).grid(row=1,column=3)
        
        root.mainloop()
    elif username.get()=="" and password.get()=="":
        messagebox.showerror("this is message","please enter username and passwrd")
    else:
        messagebox.showerror("this is message","wrong username or password")
def re():
    x=Tk()
    x.title("REGISTRATION PAGE")
    x.configure(bg="gold")
    q=StringVar()
    v=StringVar()
    w=StringVar()
    Label(x,text="First_name",bg="gold").grid(row=2)
    Label(x,text="Last_name",bg="gold").grid(row=3)
    Label(x,text="Mobile",bg="gold").grid(row=4)
    Label(x,text="Email",bg="gold").grid(row=5)
    Label(x,text="create password",bg="gold").grid(row=6)
    Label(x,text="repeat password",bg="gold").grid(row=7)
    Label(x,text="Address",bg="gold").grid(row=8)
    Label(x,text="Select gender",bg="gold").grid(row=9)
    
    Entry(x,fg="green",textvariable=q,bg="pink").grid(row=2,column=1)
    Entry(x,fg="green",textvariable=v,bg="pink").grid(row=3,column=1)
    Entry(x,fg="green",textvariable=w,bg="pink").grid(row=4,column=1)
    Entry(x,fg="green",bg="pink").grid(row=5,column=1)
    Entry(x,fg="green",bg="pink").grid(row=6,column=1)
    Entry(x,fg="green",bg="pink").grid(row=7,column=1)
    Entry(x,fg="green",bg="pink").grid(row=8,column=1)
    R1=Radiobutton(x,text="Male",value=1,bg="gold")
    R2=Radiobutton(x,text="Female",value=2,bg="gold")
    R1.grid(row=9,column=1)
    R2.grid(row=9,column=2)    
    Label(x,text="Select Language:",fg="blue",bg="gold",font=("Courier",15,"italic","bold")).grid(row=11)
    l=Listbox(x,width=20,height=4,selectmode=SINGLE)
    l.insert(1,"Hindi")
    l.insert(2,"English")
    l.insert(3,"French")
    l.insert(4,"chinese")
    l.grid(row=13)
    

    def display():
        n=Tk()
        n.geometry("600x600")
        wrapper1=LabelFrame(n,text="details of users")
        wrapper2=LabelFrame(n,text="show data")
        wrapper1.pack(fill="both",expand="yes",padx=20,pady=20)
        wrapper2.pack(fill="both",expand="yes",padx=20,pady=20)

        trv=ttk.Treeview(wrapper1, column= (1,2,3), show="headings", height="13")
        trv.pack()
        trv.heading(1, text="First_name")
        trv.heading(2, text="Last_name")
        trv.heading(3, text="Mobile")
 
   #######################################################
        def update(rows):
            for i in rows:
                trv.insert('',0,values=i)
    
################################
    
        def show():
            sql=("insert into kk1 (First_name,Last_name,Mobile) values(%s,%s,%s)")
            val=[(q.get(),v.get() ,w.get())]
            cursor.executemany(sql,val)
            con.commit()
            cursor.execute("select * from kk1")
            rows=cursor.fetchall()
            update(rows)  
        Button(wrapper2, text="Show", command=show).grid(row=5,column=0,padx=10)
        n.mainloop()
    Button(x,text="submit",bg="orange",fg="blue",activebackground="blue",font=("Courier",20,"italic","bold"),width=18,command=display).grid(row=13,column=1)
    x.mainloop()
 
Button(rahul,text="LOGIN",bg="purple",fg="white",command=login,activebackground="blue",font=("Courier",30,"italic","bold"),width=18).place(x=480,y=300)
Label(rahul,text="OR",bg="white",font=("Courier",15,"bold")).place(x=680,y=381)
Button(rahul,text="REGISTER",bg="purple",fg="white",activebackground="orange",font=("Courier",30,"italic","bold"),command=re).place(x=580,y=408)
 

rahul.mainloop()