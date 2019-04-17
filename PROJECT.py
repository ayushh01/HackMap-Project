from Tkinter import *
home=Tk()
home.title('Project')
home.config(background='maroon')
img1=PhotoImage(file='project1.gif')
l=Label(home,image=img1,bd=20,bg='maroon')
def fn(e):
    home.destroy()
    import python

l.bind('<Motion>',fn)    
l.pack()
Label(home,text='BOOK YOUR MOVIE TICKET WITH ENTERTANER',font='times 20 italic',bg='maroon',fg='black').pack()
Label(home,text='MADE BY',font='times 20 bold',bg='maroon',fg='black').pack()
Label(home,text='AYUSH SRIVASTAVA',font='Arial 15 bold',fg='black',bg='maroon').pack()
Label(home,text='171B041',font='Arial 15 bold',fg='Black',bg='maroon').pack()
Label(home,text='BX--B2',font='Arial 15 bold',fg='Black',bg='maroon').pack()


home.mainloop()
