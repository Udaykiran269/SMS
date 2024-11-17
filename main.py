from tkinter import *
from tkinter import Entry, messagebox
import ttkthemes
from tkinter import ttk

def login():
    if userName.get() == '' or password.get() == '':
        messagebox.showerror('Error', 'Fields Cannot Be Empty')

    elif userName.get() == 'Uday' and password.get() == '1234':
        messagebox.showinfo('Success', f'Welcome {userName.get()}!!')
        window.destroy()
        import SMS

    else:
        messagebox.showerror('Error', 'Incorrect Credentials')

def show():
    if val.get() == 1:
        password.config(show='') # password is visible
    else:
        password.config(show='*') # password is invisible

#GUI
window = ttkthemes.ThemedTk()
window.get_themes()
window.set_theme('radiance')
#Adjusting the Window Size to Screem
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry(f"{width}x{height}")
window.resizable(False, False)

#Window Title
window.title('SMS Login System')

#Background Image
bgImage = PhotoImage(file='Images/img_1.png')
bgLabel = Label(window, image = bgImage)
bgLabel.place(x=0, y=0)

#Frame --> for login System
loginFrame = Frame(window, bg = "white")
loginFrame.place(x=500, y=250, width=500, height=500)
    # Title & Subtitle for Frame
Label(loginFrame, text="STUDENT LOGIN SYSTEM", font=("Impact", 30, "bold"), fg="#6132FF", bg="white").place(x=60, y=30)
# Label(loginFrame, text="Student Login", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=90, y=100)

#Username
Label(loginFrame, text="UserName", font=("Goudy old style", 25, "bold"), fg="grey", bg="white").place(x=90, y=140)
userName = Entry(loginFrame, font=("times new roman", 20, 'bold'),bd = 4, bg="#E7E6E6")
userName.place(x=90, y=185, width=320, height=40)

#Password
Label(loginFrame, text="Password", font=("Goudy old style", 25, "bold"), fg="grey", bg="white").place(x=90, y=250)
password = Entry(loginFrame, show='*', font=("times new roman", 20, 'bold'),bd = 4, bg="#E7E6E6")
password.place(x=90, y=290, width=320, height=40)
val = IntVar(value=0)
c = ttk.Checkbutton(loginFrame, text='Show Password', variable=val, onvalue=1, offvalue=0, command=show)
c.place(x=90, y=340)

#Button
loginButton = ttk.Button(loginFrame, text='Login', cursor='hand2', width=25, command=login)
loginButton.place(x=150, y=370)


window.mainloop()