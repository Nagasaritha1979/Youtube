from tkinter import *
from PIL import Image,ImageTk

root=Tk()


def btn1_call():
    print("You are watching a video")
    
def btn2_call():
    print("You have clicked on Edit Button")

def btn3_call():
    print("You have clicked on Analytics Button")

def btn4_call():
    print("You have clicked on Comments Button")    

def btn5_call():
    print("You have clicked on View on YOUTUBE Button")    
    
def btn6_call():
    
    def top_btn1_call():
        pass
    tp=Toplevel(root)
    tp.geometry('400x200')
    tp.overrideredirect(1) # to remove the Toplevel window titlebar
    x = root.winfo_x()
    y = root.winfo_y()
    tp.geometry("+%d+%d" %(x+370,y+250))
    tp.config(bg='light grey')
    
    top_edit=Image.open('D://Python_programs//edit_title.png')
    top_edit_img=ImageTk.PhotoImage(top_edit)    
    
    top_btn1=Button(tp,image=top_edit_img,bd=0,bg='light grey',activebackground='light grey')
    top_btn1.place(x=0,y=0)
    top_btn1.image=top_edit_img
    
    promote=Image.open('D:\\Python_Programs\\promote.png')
    promote_img=ImageTk.PhotoImage(promote)
    
    top_btn2=Button(tp,image=promote_img,bd=0,bg='light grey',activebackground='light grey')
    top_btn2.place(x=0,y=50)
    top_btn2.image=promote_img
    
    download=Image.open('D:\\Python_Programs\\download.png')
    download_img=ImageTk.PhotoImage(download)
    
    top_btn3=Button(tp,image=download_img,bd=0,bg='light grey',activebackground='light grey')
    top_btn3.image=download_img
    top_btn3.place(x=0,y=100)
    
    delete=Image.open('D:\\Python_Programs\\delete.png')
    delete_img=ImageTk.PhotoImage(delete)
    
    top_btn4=Button(tp,image=delete_img,bg='light grey',activebackground='light grey',bd=0)
    top_btn4.image=delete_img
    top_btn4.place(x=0,y=150)
      
    

    
    print('You have clicked the Options button')
    
def call(e):
    b2=Button(b1,image=edit_img1,bg='red',activebackground='red',command=btn2_call,bd=0)
    b2.place(x=2,y=220) 
    
    b3=Button(b1,image=analytics_img1,bg='red',activebackground='red',bd=0,command=btn3_call)
    b3.place(x=105,y=220) 
    
    b4=Button(b1,image=comments_img1,bg='red',activebackground='red',bd=0,command=btn4_call)
    b4.place(x=255,y=220) 
    
    b5=Button(b1,image=yt_img1,bg='red',activebackground='red',bd=0,command=btn5_call)
    b5.place(x=425,y=220)
    
    b6=Button(b1,image=options_img1,bg='red',activebackground='red',bd=0,command=btn6_call)
    b6.place(x=650,y=220)
    
    
b1=Button(root,height=15,width=100,activebackground='red',bg='red',text="Video - 1",fg='white',font=("Calibri",12,'bold'),command=btn1_call)
b1.place(x=0,y=0)
edit_img=Image.open('D://Python_Programs//edit.png')
edit_img1=ImageTk.PhotoImage(edit_img,master=b1)

analytics_img=Image.open('D://Python_Programs//analytics.png')
analytics_img1=ImageTk.PhotoImage(analytics_img,master=b1)

comments_img=Image.open('D://Python_Programs//comments.png')
comments_img1=ImageTk.PhotoImage(comments_img,master=b1)

yt_img=Image.open('D://Python_Programs//yt.png')
yt_img1=ImageTk.PhotoImage(yt_img,master=b1)

options_img=Image.open('D://Python_Programs//options.png')
options_img1=ImageTk.PhotoImage(options_img,master=b1)


b1.bind("<Enter>", call)

root.mainloop()
