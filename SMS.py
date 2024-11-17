import pandas as pd
import time
from tkinter import *
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql


#Functionality
def topleveldata(windtitle, btntext, fun):
    global wind,identry, nameentry, phoneentry, emailentry, addressentry, genderentry, dobentry

    wind = Toplevel()
    wind.title(windtitle, )
    wind.resizable(False, False)
    wind.grab_set()

    idlabel = Label(wind, text='Roll_No', font=('times new roman', 20, 'bold'))
    idlabel.grid(row=0, column=0, padx=30, pady=20, sticky=W)
    identry = Entry(wind, font=('roman', 15, 'bold'))
    identry.grid(row=0, column=1, pady=20, padx=15)

    namelabel = Label(wind, text='Name', font=('times new roman', 20, 'bold'))
    namelabel.grid(row=1, column=0, padx=30, pady=20, sticky=W)
    nameentry = Entry(wind, font=('roman', 15, 'bold'))
    nameentry.grid(row=1, column=1, pady=20, padx=15)

    phonelabel = Label(wind, text='Phone_No', font=('times new roman', 20, 'bold'))
    phonelabel.grid(row=2, column=0, padx=30, pady=20, sticky=W)
    phoneentry = Entry(wind, font=('roman', 15, 'bold'))
    phoneentry.grid(row=2, column=1, pady=20, padx=15)

    emaillabel = Label(wind, text='Email', font=('times new roman', 20, 'bold'))
    emaillabel.grid(row=3, column=0, padx=30, pady=20, sticky=W)
    emailentry = Entry(wind, font=('roman', 15, 'bold'))
    emailentry.grid(row=3, column=1, pady=20, padx=15)

    addresslabel = Label(wind, text='Address', font=('times new roman', 20, 'bold'))
    addresslabel.grid(row=4, column=0, padx=30, pady=20, sticky=W)
    addressentry = Entry(wind, font=('roman', 15, 'bold'))
    addressentry.grid(row=4, column=1, pady=20, padx=15)

    genderlabel = Label(wind, text='Gender', font=('times new roman', 20, 'bold'))
    genderlabel.grid(row=5, column=0, padx=30, pady=20, sticky=W)
    genderentry = Entry(wind, font=('roman', 15, 'bold'))
    genderentry.grid(row=5, column=1, pady=20, padx=15)

    doblabel = Label(wind, text='DoB', font=('times new roman', 20, 'bold'))
    doblabel.grid(row=6, column=0, padx=30, pady=20, sticky=W)
    dobentry = Entry(wind, font=('roman', 15, 'bold'))
    dobentry.grid(row=6, column=1, pady=20, padx=15)

    button = ttk.Button(wind, text=btntext, command=fun)
    button.grid(row=7, columnspan=2, pady=10)

    if windtitle=='UPDATE STUDENT DETAILS':
        try:
            # Updated Rows
            i = studentTable.focus()
            content = studentTable.item(i)
            datalist = content['values']
            identry.insert(0, datalist[0])
            nameentry.insert(0, datalist[1])
            phoneentry.insert(0, datalist[2])
            emailentry.insert(0, datalist[3])
            addressentry.insert(0, datalist[4])
            genderentry.insert(0, datalist[5])
            dobentry.insert(0, datalist[6])
        except:
            wind.destroy()
            messagebox.showerror('Error', 'First select the record and then click on Delete Student Button')

def export_data():
    try:
        url = filedialog.asksaveasfilename(defaultextension='.csv')
        indexing = studentTable.get_children()
        newlist = []
        for i in indexing:
            contents = studentTable.item(i)
            newlist.append(contents['values'])
        table = pd.DataFrame(newlist, columns=['Roll_NO', 'Name', 'Mobile_No', 'Email', 'Address', 'Gender','DoB','AddedDate', 'AddedTime'])
        table.to_csv(url, index=False)
        messagebox.showinfo('Success', f'Data Saved Successfully on {url}!!')
    except:
        pass

def exit():
    res = messagebox.askyesno('Confirm', 'Do You Want to Exit!!')
    if res:
        root.destroy()
    else:
        pass

def connect_database():
    def connect():
        try:
            conn = pymysql.connect(host='localhost', user='root', password='Uday@2002')
            mycursor = conn.cursor()

        except:
            messagebox.showerror('Error', 'Invalid Details', parent=connectWindow)
            return
        try:
            query = 'CREATE DATABASE StudentData'
            mycursor.execute(query)
            query = 'USE StudentData'
            mycursor.execute(query)
            query = ('CREATE TABLE (Roll_no varchar(30) PRIMARY KEY, name VARCHAR(30), Mobile_no VARCHAR(10), email VARCHAR(30), Address VARCHAR(100), '
                     'gender VARCHAR(6), Dob VARCHAR(30), addedDate VARCHAR(30), addedTime VARCHAR(30)')
            mycursor.execute(query)
        except:
            query = 'USE StudentData'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'DataBase Connection is Successful', parent=connectWindow)
        connectWindow.destroy()

        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        exitstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        conn.close()

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x300+730+230')
    connectWindow.title("DataBase Connection")
    connectWindow.resizable(False, False)

    #Window attributes
    hostnamelabel = Label(connectWindow, text="  Host Name", font=('arial', 20, 'bold'))
    hostnamelabel.grid(row=0, column=0)
    hostentry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    hostentry.grid(row=0, column=1, padx = 40, pady = 20)

    usernamelabel = Label(connectWindow, text="  User Name", font=('arial', 20, 'bold'))
    usernamelabel.grid(row=1, column=0)
    userentry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    userentry.grid(row=1, column=1, padx=40, pady=20)

    passwordlabel = Label(connectWindow, text="Password", font=('arial', 20, 'bold'))
    passwordlabel.grid(row=2, column=0)
    passwordentry = Entry(connectWindow, show='*',font=('roman', 15, 'bold'), bd=2)
    passwordentry.grid(row=2, column=1, padx=40, pady=20)

    val = IntVar(value=0)

    def show():
        if val.get() == 1:
            passwordentry.config(show='')  # password is visible
        else:
            passwordentry.config(show='*')  # password is invisible
    c = ttk.Checkbutton(connectWindow, text='Show Password', variable=val, onvalue=1, offvalue=0, command=show)
    c.grid(row=3, column=0)

    connectbutton = ttk.Button(connectWindow, text='Connect', command=connect)
    connectbutton.grid(row=4, column=1)



def add_data():
    conn = pymysql.connect(host='localhost', user='root', password='Uday@2002')
    mycursor = conn.cursor()
    query = 'USE StudentData'
    mycursor.execute(query)
    if identry.get() == '' or nameentry.get() == '' or phoneentry.get() == '' or emailentry.get() == '' or addressentry.get() =='' or genderentry.get() == '' or dobentry.get() == '':
        messagebox.showerror('Error', 'All fields are Required', parent=wind)

    else:
        try:
            currdate = time.strftime('%d/%m/%Y')
            currtime = time.strftime('%H:%M:%S')
            query = 'INSERT INTO STUDENT VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            mycursor.execute(query, (identry.get(), nameentry.get(), phoneentry.get(), emailentry.get(), addressentry.get(), genderentry.get(), dobentry.get(), currdate, currtime))
            conn.commit()
            result = messagebox.askyesno('Confirmation','Data Inserted Successfully.Do You want to clean the form?', parent=wind)
            if result:
                identry.delete(0, END)
                nameentry.delete(0, END)
                phoneentry.delete(0, END)
                emailentry.delete(0, END)
                addressentry.delete(0, END)
                genderentry.delete(0, END)
                dobentry.delete(0, END)
            else:
                pass
        except:
            messagebox.showerror('Error', 'Duplicate Roll No. Does not Exist', parent=wind)
            return

    query = 'SELECT *  FROM STUDENT'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        datalist = list(data)
        studentTable.insert('', END, values=datalist)




def search_data():
    conn = pymysql.connect(host='localhost', user='root', password='Uday@2002')
    mycursor = conn.cursor()
    query = 'USE StudentData'
    mycursor.execute(query)

    query = 'SELECT * FROM student WHERE Roll_No=%s or name = %s or address = %s or gender = %s'
    mycursor.execute(query, (identry.get(), nameentry.get(), addressentry.get(), genderentry.get()))
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())

    for data in fetched_data:
        datalist = list(data)
        studentTable.insert('', END, values=datalist)
    wind.destroy()



def show_students():
    conn = pymysql.connect(host='localhost', user='root', password='Uday@2002')
    mycursor = conn.cursor()
    query = 'USE StudentData'
    mycursor.execute(query)

    query = 'SELECT * FROM student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())

    for data in fetched_data:
        datalist = list(data)
        studentTable.insert('', END, values=datalist)


def delete_student():
    try:
        i = studentTable.focus()
        content = studentTable.item(i)
        content_id = content['values'][0]
        conn = pymysql.connect(host='localhost', user='root', password='Uday@2002')
        mycursor = conn.cursor()
        query = 'USE StudentData'
        mycursor.execute(query)
        query = 'DELETE FROM STUDENT WHERE Roll_No = %s'
        mycursor.execute(query, content_id)
        conn.commit()
        messagebox.showinfo('Deleted', f'{content_id} student record is deleted successfully!!')

        query = 'SELECT * FROM student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())

        for data in fetched_data:
            datalist = list(data)
            studentTable.insert('', END, values=datalist)
    except:
        messagebox.showerror('Error','First select the record and then click on Delete Student Button')



def update_data():
    currdate = time.strftime('%d/%m/%Y')
    currtime = time.strftime('%H:%M:%S')

    conn = pymysql.connect(host='localhost', user='root', password='Uday@2002')
    mycursor = conn.cursor()
    query = 'USE StudentData'
    mycursor.execute(query)


    if identry.get() == '' or nameentry.get() == '' or phoneentry.get() == '' or emailentry.get() == '' or addressentry.get() =='' or genderentry.get() == '' or dobentry.get() == '':
        messagebox.showerror('Error', 'All fields are Required', parent=wind)
    else:
        query = 'UPDATE STUDENT SET name=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s, addedDate=%s, addedTime=%s WHERE Roll_No=%s'
        mycursor.execute(query, (nameentry.get(), phoneentry.get(), emailentry.get(), addressentry.get(), genderentry.get(), dobentry.get(), currdate, currtime, identry.get()))
        conn.commit()
        messagebox.showinfo('Success', f'Id {identry.get()} is modified successfully', parent=wind)
    wind.destroy()
    show_students()


def clock():
    global datetimelabel
    date = time.strftime('%d-%m-%Y')
    currTime = time.strftime('%H:%M:%S')
    datetimelabel.config(text=f'    Date : {date}\nTime : {currTime}')
    datetimelabel.after(1000, clock)


ind, sliderText = 0, ''
def slider():
    global s, sliderLabel, sliderText, ind
    if ind == len(s):
        ind = 0
        sliderText = ''
    sliderText += s[ind]
    sliderLabel.config(text=sliderText)
    ind += 1
    sliderLabel.after(175, slider)




#GUI

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
#Adjusting the Window Size to Screem
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry(f"{width}x{height}")
root.resizable(False, False)

#Window Title
root.title('Student Management System')

#Date Time
datetimelabel = Label(root, text="Hello",font=("times new roman", 25, "bold"))
datetimelabel.place(x=5, y=10)
clock()

#Slider
sliderLabel = Label(root, font=("ariel", 25, "italic bold"), fg="red",width=50)
sliderLabel.place(x=300, y=10)
s = 'STUDENT MANAGEMENT SYSTEM'
slider()

#Button
connectButton = ttk.Button(root, text='Connect To Database', command=connect_database)
connectButton.place(x=1200, y=15)

#LEFT Frame
leftFrame = Frame(root)
leftFrame.place(x=100, y=150, width=300, height=864)

logo_image = PhotoImage(file='Images/Students.png')
logo_label = Label(leftFrame, image=logo_image)
logo_label.grid(row=0, column=0)
    # Button
addstudentButton = ttk.Button(leftFrame, text='Add Student', width=25, state=DISABLED, command=lambda : topleveldata('ADD STUDENT DETAILS','ADD STUDENT', add_data))
addstudentButton.grid(row=1, column=0, pady = 10)

searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=25, state=DISABLED, command=lambda : topleveldata('SEARCH STUDENT DETAILS','SEARCH', search_data))
searchstudentButton.grid(row=2, column=0, pady = 10)

showstudentButton = ttk.Button(leftFrame, text='Show Student', width=25, state=DISABLED, command=show_students)
showstudentButton.grid(row=3, column=0, pady = 10)

updatestudentButton = ttk.Button(leftFrame, text='Update Student', width=25, state=DISABLED, command=lambda : topleveldata('UPDATE STUDENT DETAILS','UPDATE', update_data))
updatestudentButton.grid(row=4, column=0, pady = 10)

deletestudentButton = ttk.Button(leftFrame, text='Delete Student', width=25, state=DISABLED, command=delete_student)
deletestudentButton.grid(row=5, column=0, pady = 10)

exportstudentButton = ttk.Button(leftFrame, text='Export Data', width=25, state=DISABLED, command=export_data)
exportstudentButton.grid(row=6, column=0, pady = 10)

exitstudentButton = ttk.Button(leftFrame, text='Exit', width=25, state=DISABLED, command=exit)
exitstudentButton.grid(row=7, column=0, pady = 10)


#RIGHT Frame
rightFrame = Frame(root)
rightFrame.place(x=350, y=150, width=1100, height=500)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

#TreeView
studentTable = ttk.Treeview(rightFrame, columns=('Roll No', 'Name', 'Mobile No', 'Email','Address', 'Gender', 'DD/MM/YYYY',
                                  'Added Date', 'Added Time'), xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

studentTable.pack(fill=BOTH, expand=1)


#Adding Columns to the Student Table

studentTable.heading('Roll No', text='Roll No')
studentTable.heading('Name', text='Name')
studentTable.heading('Mobile No', text='Mobile No')
studentTable.heading('Email', text='Email')
studentTable.heading('Address', text='Address')
studentTable.heading('Gender', text='Gender')
studentTable.heading('DD/MM/YYYY', text='DD/MM/YYYY')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')
studentTable.config(show='headings')

studentTable.column('Roll No', width=200, anchor=CENTER)
studentTable.column('Name', width=200, anchor=CENTER)
studentTable.column('Mobile No', width=200, anchor=CENTER)
studentTable.column('Email', width=300, anchor=CENTER)
studentTable.column('Address', width=200, anchor=CENTER)
studentTable.column('Gender', width=100, anchor=CENTER)
studentTable.column('DD/MM/YYYY', width=200, anchor=CENTER)
studentTable.column('Added Date', width=200, anchor=CENTER)
studentTable.column('Added Time', width=200, anchor=CENTER)

style = ttk.Style()
style.configure('Treeview', rowheight=30, font=('arial',13,'bold'), backgroun='white',foreground='black')
style.configure('Treeview.Heading', font=('arial', 15, 'bold'), foreground='green')
studentTable.config(show='headings')


root.mainloop()


