from tkinter import *
import tkinter  as tk
from PIL import ImageTk
from tkinter import messagebox
import os
import smtplib
import datetime as d
from subprocess import  call


from time import strftime

class login_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1199x600")
        self.root.title("Food Ordering System")
        #--------------------------------BACKGROUND_IMAGE-----------------------------------------------------------------------#
        self.bg = ImageTk.PhotoImage(file="images/background3 (1).jpg")
        self.b_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #---------------------------------LOGIN_FRAME----------------------------------------------------------------------------#
        framelog = Frame(self.root, bg="purple")
        framelog.place(x=550, y=150, height=300, width=400)
        title = Label(framelog, text="Welcome", font=("italic", 35, "bold"), fg="#d77337", bg="purple").place(x=90, y=30)
        desc = Label(framelog, text="For Accountant Employee", font=("Goudy old style", 15, "bold"), fg="#d25d17",bg="purple").place(x=90, y=100)

        #---------------------------------EMPLOYEE_LABEL--------------------------------------------------------------------------#
        lb_Empid = Label(framelog, text="Emp Id", font=("Goudy old style", 15, "bold"), fg="white", bg="purple").place(x=90, y=140)
        self.txt_Empid = Entry(framelog, font=("times new roman", 15))
        self.txt_Empid.place(x=90, y=170, width=150, height=20)

        # ---------------------------------PASSWORD_LABEL--------------------------------------------------------------------------#
        lb_pass = Label(framelog, text="Password", font=("Goudy old style", 15, "bold"), fg="white", bg="purple").place(x=90, y=190)
        self.txt_pass = Entry(framelog, show="*", width=20)
        self.txt_pass.place(x=90, y=220, width=150, height=20)

        #---------------------------------LOGIN_BUTTON------------------------------------------------------------------------------#
        login_b = Button(self.root, command=self.login_func, text="Login", cursor="hand2", fg="white", bg="purple",font=("times new roman", 15)).place(x=580, y=400, width=180, height=40)

        def exit():
            root.destroy()
        login_b = Button(self.root, command=exit, text="Exit", cursor="hand2", fg="white", bg="purple",font=("times new roman", 15)).place(x=765, y=400, width=180, height=40)
        #---------------------------------TIME_DATE_DAY-----------------------------------------------------------------------------#
        date = d.datetime.now()
        label2 = Label(root, text=f"{date: %x \t %A \t%H:%M %p}",bg="coral",font="Calibri, 20").place(x=167, y=10)

    #-------------------------------------LOGIN_FUNCTION-----------------------------------------------------------------------------#
    def login_func(self):

        if self.txt_pass.get() == "" or self.txt_Empid.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_pass.get() != "1" or self.txt_Empid.get() != "s":
            messagebox.showinfo("Error", "Invalid Username/Password", parent=self.root)
        else:
            root.destroy()
            import menu as mn









root = Tk()
b1 = login_system(root)
root.state("zoomed")
root.mainloop()
