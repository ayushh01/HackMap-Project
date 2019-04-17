from Tkinter import *
from tkMessageBox import*
import sqlite3
con=sqlite3.Connection('Project100.db')
cur=con.cursor()
cur.execute("create table if not exists login19(name varchar2(20),cardnumber varchar(15),pin varchar(15),password varchar(15))")
con.commit()
root=Tk()
root.title('Movie Ticket Booking')
root.config(background="sky blue")
Label(root,text='WELCOME TO ENTERTANIER',font="Arial 20 bold",bg="Light Blue").pack()
img1=PhotoImage(file='project.gif')
Label(root,image=img1).pack()
global img2
img2=PhotoImage(file='movieposter1.gif')
global img3
img3=PhotoImage(file='movieposter2.gif')

def fun():
    root1=Tk()
    root1.title('Login Page')
    root1.config(background="sky blue")
    root1.geometry("500x400")

    
    
    Label(root1,text='Login Page',font="times 20 bold",bg="sky blue",fg="red").grid(row=0,column=5,columnspan=4)
    Label(root1,font="times 20 bold",bg="sky blue").grid(row=1,column=1)
    Label(root1,text='USERNAME:--',font="times 15 bold",bg="sky blue",fg="red").grid(row=2,column=3)
    Label(root1,font="times 20 bold",bg="sky blue").grid(row=2,column=4)
    e1=Entry(root1,font="times 15 bold",width=20,bg="Light grey",bd=5)
    e1.grid(row=2,column=5)
    Label(root1,font="times 20 bold",bg="sky blue").grid(row=3,column=1)
    Label(root1,text='PASSWORD:--',font="times 15 bold",bg="sky blue",fg="red").grid(row=4,column=3)
    Label(root1,font="times 20 bold",bg="sky blue").grid(row=4,column=4)
    e2=Entry(root1,font="times 15 bold",width=20,bg="Light grey",show='*',bd=5)
    e2.grid(row=4,column=5)
    Label(root1,font="times 20 bold",bg="sky blue").grid(row=5,column=1)
   
    def fun2():
        if (len(e1.get())==0):
            showerror('Warning',"Box is Empty! Write username and password Correctly")
        elif(len(e2.get())==0):
            showerror('Warning',"Box is Empty! Write username and password Correctly")
        else:
            #root1.destroy()
            showinfo('sucess','login Succesfully')
            root2=Toplevel()
            root2.title('Movie Ticket Booking')
            root2.geometry("600x400")
            root2.config(background="sky blue")
    
            Label(root2,text='BOOK YOUR TICKET',font="times 20 bold",bg="sky blue",fg="red").grid(row=0,column=1,columnspan=8)
            Label(root2,font="times 20 bold",bg="sky blue").grid(row=1,column=0)
            Label(root2,text='Enter Your City',font="times 20 bold",bg="sky blue",fg="red").grid(row=3,column=0)
            e3=Entry(root2,font="times 20 bold",width=20,justify="right",bd=5)
            e3.grid(row=3,column=1)
            Label(root2,text=e1.get()+'  WELCOME   ',font='Arial 15 bold',bg="sky blue",fg="Blue").grid(row=2,column=1)
            def fun3():
                root3=Tk()
                root3.title('BOOK YOUR TICKET')
                root3.config(background="sky blue")
    
                Label(root3,text='BOOK YOUR TICKET',font="times 20 bold",bg="sky blue").grid(row=0,column=2,columnspan=8)
                Label(root3,text='      ',font="times 20 bold",bg="sky blue").grid(row=1,column=0)
                Label(root3,text=' Halls in  '+e3.get()+':-- ',font="Arial 15 bold",fg="red",bg="sky blue").grid(row=2,column=1)
                Label(root3,text='      ',font="times 20 bold",bg="sky blue").grid(row=3,column=0)
                Label(root3,text='CITY Hall 1',font="times 10 bold",bg="sky blue").grid(row=4,column=1)


                def fun4():
                    
                    root3.destroy()
                    root4=Tk()
                    root4.title('HALL SEATS')
                    root4.geometry('500x400')
                    root4.config(background="sky blue")
                    Label(root4,text="   ",font='times 20 bold',bg="sky blue").grid(row=0,column=0)
                    Label(root4,text='------------------------------------------------------------------------',bg="sky blue").grid(row=2,column=1,columnspan=5)
                    Label(root4,text='                               SCREEN                                   ',font='times 20 bold',bg="sky blue").grid(row=3,column=1,columnspan=5)                                  
                    Label(root4,text="   ",font='times 20 bold',bg="sky blue").grid(row=4,column=0)
                    def fun5():
                        #name=StringVar()
                        #cardno=IntVar()
                        #pin=IntVar()
                        #password=StringVar()
                        root4.destroy()
                        root5=Tk()
                        root5.title('PAYMENT')
                        root5.config(background="sky blue")
                        global name
                        global cardno
                        global pin
                        global password
                        Label(root5,text='CONFIRM AND PAY',font='Arial 20 bold',fg='Blue',bg="sky blue").grid(row=0,column=1)
                        Label(root5,text="   ",font='times 20 bold',bg="sky blue").grid(row=1,column=0)
                        Label(root5,text='Enter Your Name ',font='times 20 bold',bg="sky blue").grid(row=2,column=0)
                        Label(root5,text="   ",font='times 20 bold',bg="sky blue").grid(row=2,column=1)
                        name=Entry(root5,font='Arial 15 bold',width=20,bd=5)
                        name.grid(row=2,column=2)
                        Label(root5,text="   ",font='times 20 bold',bg="sky blue").grid(row=3,column=0)
                        Label(root5,text='CARD NUMBER ',font='times 20 bold',bg="sky blue").grid(row=4,column=0)
                        Label(root5,text="   ",font='times 20 bold',bg="sky blue").grid(row=4,column=1)
                        cardno=Entry(root5,font='Arial 15 bold',width=20,bd=5)
                        cardno.grid(row=4,column=2)
                        Label(root5,text="   ",font='times 20 bold',bg="sky blue").grid(row=5,column=0)
                        Label(root5,text='PIN ',font='times 20 bold',bg="sky blue").grid(row=6,column=0)
                        Label(root5,text="   ",font='times 20 bold',bg="sky blue").grid(row=6,column=1)
                        pin=Entry(root5,font='Arial 15 bold',width=20,bd=5)
                        pin.grid(row=6,column=2)
                        
                        Label(root5,text="   ",font='times 20 bold',bg="sky blue").grid(row=7,column=0)
                        Label(root5,text='SET a Password ',font='times 20 bold',bg="sky blue").grid(row=8,column=0)
                        Label(root5,text="   ",font='times 20 bold',bg="sky blue").grid(row=8,column=1)
                        password=Entry(root5,font='Arial 15 bold',width=20,bd=5)
                        password.grid(row=8,column=2)

                         
                        Label(root5,text="   ",font='times 20 bold',bg="sky blue").grid(row=9,column=0)
                        Label(root5,text='TOTAL',font='Arial 20 bold',bg="sky blue").grid(row=10,column=0)
                        Label(root5,text='300',font='Arial 20 bold',bg="sky blue").grid(row=10,column=2)
                        Label(root5,text="   ",font='times 20 bold',bg="sky blue").grid(row=11,column=0)
                        Label(root5,text="PLEASE REMEMBER THE PASSWORD ",font="Arial 20 bold",bg="sky blue").grid(row=12,column=0,columnspan=3)
                        Label(root5,text="SO YOU MAY CHECK YOUR BOOKING STATUS",font="Arial 20 bold",bg="sky blue").grid(row=13,column=0,columnspan=5)
                        Label(root5,font="times 20 bold",bg="sky blue").grid(row=14,column=0)
                        
                        
                        def fun6():
                            #a=[(name.get(),cardno.get(),pin.get(),password.get())]
                            #con=sqlite3.Connection('Project10.db')
                            cur=con.cursor()
                            cur.execute("insert into login19 values(?,?,?,?)",(name.get(),cardno.get(),pin.get(),password.get()))
                            con.commit()
                            showinfo('Booked',"your Ticket is Booked now")
                        Button(root5,text='PAY',font='times 15 bold',command=fun6,bd=5,width=20,height=2).grid(row=15,column=1)
                        
                        



                    
                    Button(root4,text="SEAT A1",font='times 15 bold',command=fun5,bd=5).grid(row=5,column=1)                                 
                    Label(root4,text="   ",font='times 20 bold',bg="sky blue").grid(row=6,column=0)
                    Button(root4,text="SEAT A3",font='times 15 bold',command=fun5,bd=5).grid(row=7,column=1)                                 
                    Label(root4,text="   ",font='times 20 bold',bg="sky blue").grid(row=8,column=0)
                    Button(root4,text="SEAT A5",font='times 15 bold',command=fun5,bd=5).grid(row=9,column=1)
            
                    Button(root4,text="SEAT A2",font='times 15 bold',command=fun5,bd=5).grid(row=5,column=2)                                 
                    
                    Button(root4,text="SEAT A4",font='times 15 bold',command=fun5,bd=5).grid(row=7,column=2)                                 
                    
                    Button(root4,text="SEAT A6",font='times 15 bold',command=fun5,bd=5).grid(row=9,column=2)
                
            
                
                
            
                
                
            
                Button(root3,text='BOOK',width=15,height=2,command=fun4,bd=5).grid(row=4,column=2)
                Label(root3,text='      ',font="times 20 bold",bg="sky blue").grid(row=5,column=0)
                Label(root3,text='CITY Hall 2',font="times 10 bold",bg="sky blue").grid(row=6,column=1)
               
                

            
                Button(root3,text='BOOK',width=15,height=2,command=fun4,bd=5).grid(row=6,column=2)

                

        
                #root3.mainloop()


        
            Button(root2,text='Search',width=15,height=2,command=fun3,bd=5).grid(row=3,column=2)
            img2=PhotoImage(file='movieposter1.gif')
            img3=PhotoImage(file='movieposter2.gif')

          
            Label(root2,image=img2).grid(row=4,column=0)
            Label(root2,image=img3).grid(row=4,column=1)
        
            root2.mainloop()
    
    Button(root1,text='Login',width=10,height=2,bg="yellow",command=fun2,bd=5).grid(row=6,column=5)

      
    #root1.mainloop()
def newfun():
    global j1
    global j
    check=StringVar()
    root6=Tk()
    root6.title('ENTERTANER')
    root6.geometry('800x400')
    root6.config(background='maroon')
    Label(root6,text='YOUR PAST BOOKING',font='Arial 20 bold',fg="black",bg='maroon').pack()
    Label(root6,font='Arial 20 bold',bg='maroon').pack()
    Label(root6,text='Enter your password that you put at the time of Booking:--',font='Arial 15 bold',bg='maroon',fg='black').pack()
    Label(root6,font='times 15 bold',bg='maroon').pack()
    j=Entry(root6,text='Arial 20 bold',bd=5,width=30)
    j.pack()
    Label(root6,font='times 15 bold',bg='maroon').pack()
    #j=check.get()
    def newfun2():
        root7=Tk()
        root7.geometry('400x400')
        root7.title('ENTERTANER')
        root7.config(background='maroon')
        j1=j.get()
        #con=sqlite3.Connection('Project10.db')
        cur=con.cursor()
        cur.execute("select * from login19 where password is (?)",(j1,))
        x=cur.fetchall()
        #print (x)
        Label(root7,text='YOU BOOKING DETAILS',font='Arial 20 bold',bg='maroon').pack()
        Label(root7,font="times 15 bold",bg='maroon').pack()
        Label(root7,text='THANK YOU',font="times 15 bold",bg='maroon').pack()
        Label(root7,text=x[0],font='times 15 bold',bg='maroon').pack()
        Label(root7,text='SEAT BOOKED',font='times 15 bold',bg='maroon').pack()
        Label(root7,text='You Paid 300',font='times 15 bold',bg='maroon').pack()
        con.commit()
        root7.mainloop()
    Button(root6,text='CHECK',width=10,height=2,command=newfun2,bd=5).pack()
    root6.mainloop()
    


Button(root,text='START YOUR BOOKING',width=30,height=2,bg="light green",command=fun,bd=5).pack()
Button(root,text='CHECK YOUR BOOKING STATUS',width=40,height=2,bg="light green",command=newfun,bd=5).pack()



mainloop()
