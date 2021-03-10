from tkinter import *
from tkinter import ttk
from tkinter import messagebox, scrolledtext,Label
import mysql.connector
import re
from docx import Document
import os
from PIL import ImageTk, Image
root = Tk()
root.title("Dashboard")
root.geometry("2000x800")

v_country = StringVar()
v_emailId = StringVar()
v_detaileddescription = StringVar()


def db():
    Country = v_country.get()
    Email_ID = v_emailId.get()
    Description = v_detaileddescription.get()
    conn = mysql.connector.connect(host="localhost", user="root", passwd="Zaroon@786", database="sakila",auth_plugin="mysql_native_password")
    cursor = conn.cursor()
    # cursor.execute("Create table member3(Country varchar(200), Email_ID varchar(200), Description varchar(200) )")
    cursor.execute('INSERT INTO member5(Country,Email_ID,Description) VALUES(%s,%s,%s)',(Country, Email_ID, Description))
    # t=(Country,Email_ID,Description,Description)
    # s="update member2 set Country=%s,Email_ID=%s,Description=%s where Description=%s"
    # cursor.execute()
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    print("Query Executed successfully")
    conn.commit()


def show():
    conn = mysql.connector.connect(host="localhost", user="root", passwd="Zaroon@786", database="sakila",auth_plugin="mysql_native_password")
    cursor = conn.cursor()
    # cursor.execute("Create table member3(Country varchar(200), Email_ID varchar(200), Description varchar(200) )")
    cursor.execute("Select e1.CapabilityID ,e1.DomainName,e1.OrganizationName,e1.PointofContact,e1.OrganizationAddress,e1.ContactNumber,e2.Country,e2.Email_ID,e2.Description from member4 as e1 inner join member5 as e2 on e1.id=e2.id")
    # t=(Country,Email_ID,Description,Description)
    # s="update member2 set Country=%s,Email_ID=%s,Description=%s where Description=%s"
    # cursor.execute()
    myresult = cursor.fetchall()
    for x in myresult:
        cap = x[0]
        do = x[1]
        con = x[2]
        em = x[3]
        vm = x[4]
        ab = x[5]
        cd = x[6]
        ef = x[7]
        gh = x[8]
        txt.insert(INSERT, '\n'+cap+'\t\t'+do+'\t\t'+con+'\t\t'+em+'\t\t'+vm+'\t\t'+ab+'\t\t'+cd+'\t\t'+ef+'\t\t'+gh)

    conn.close()


def click():
    doc = Document()
    with open("records.txt", 'r', encoding='utf-8') as file:
        doc.add_paragraph(file.read())
    doc.save(r"C:\Users\lenovo\PycharmProjects\tut\Cae.docx")
    os.startfile(r"C:\Users\lenovo\PycharmProjects\tut\Cae.docx")


def callOldScreen():
    root.destroy()
    os.system('python new5.py')


def callScreen():
    root.destroy()
    os.system('python new6.py')

def isValidEmail(user_email):
    print(user_email)
    if len(user_email) > 7:
        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[_a-z0-9-]+)*(\.[a-z]{2,4})$', user_email) != None:
            return True
        else:
            messagebox.showinfo('Information', 'This is not a Valid Email address')
            return False
    else:
        messagebox.showinfo('Information', 'This is not a Valid Email address')
        return False


def validateallfields():
    if v_emailId.get() == "":
        messagebox.showinfo('Information', 'Please Enter Email ID to proceed')
    elif v_detaileddescription.get() == "":
        messagebox.showinfo('Information', 'Please enter description to proceed')
    elif v_emailId.get() != "":
        status = isValidEmail(v_emailId.get())
        if status:
            messagebox.showinfo('Information', 'Client Registered Successfully')
    else:
        messagebox.showinfo('Information', 'Client Registered Successfully')


def getvals():
    print("Submitting form")
    print(f"{v_country.get(), v_emailId.get(), v_detaileddescription.get()} ")

    with open("records.txt", "a") as f:
        # f.write(f"\r\n\t\t\t\t COMPLIANCE ASSESSMENT REPORT" "\r\n")
        f.write(f"\r\nCountry: " + v_country.get() + "\r\n")
        f.write(f"\r\nEmail ID: " + v_emailId.get() + "\r\n")
        f.write(f"\r\nDetailed Description: " + v_detaileddescription.get() + "\r\n")


canv = Canvas(master=root)
canv.place(x=0, y=0, width=1600, height=799)

img = ImageTk.PhotoImage(Image.open("black.jpg"))  # <-- PIL
canv.create_image(0, 0, image=img, anchor='nw')


Label(root, text="XentIT FedRAMP & CMMC Compliance", bg="black", fg="orange", width=40, height=2,font=('comicsansms', 30, 'italic bold underline')).place(x=250, y=2)

lb_country = Label(root, text="Country", width=15, height=1, fg="black", bg="white", font=('times', 15, ' bold '))
lb_country.place(x=380, y=150)
list_country = ['Berlin', 'Norway', 'Austria', 'England', 'United States', 'Saudi Arabia', 'United Arab Emirates','Canada', 'Russia', 'China']
droplist = OptionMenu(root, v_country, *list_country)
droplist.config(textvariable=v_country, width=20, height=1, fg="black", bg="white", font=('times', 12, ' bold '))
v_country.set('Select Your Country')
droplist.place(x=850, y=150)

lb_email = Label(root, text="Email", width=15, height=1, fg="black", bg="white", font=('times', 15, ' bold '))
lb_email.place(x=380, y=200)
entry_email = Entry(root, textvariable=v_emailId, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
entry_email.place(x=850, y=200)


l1 = Label(root, text="Detailed Description", width=15, height=1, fg="black", bg="white", font=('times', 15, ' bold '))
l1.place(x=380, y=250)
textbox = Entry(root, textvariable=v_detaileddescription, width=20, fg="black", bg="white",font=('times', 15, ' bold '))
textbox.place(x=850, y=250)


Button1 = Button(root, text="Proceed", command=callScreen, width=10, bg="dark blue", fg="white",activebackground="#1F618D", activeforeground="white", font=('times', 15, ' bold '))
Button1.place(x=850, y=520)

button2 = Button(root, text="SAVE", command=lambda: [validateallfields(), getvals(), db()], width=10, bg="dark blue",fg="white", activebackground="#FF0000", activeforeground="white", font=('times', 15, ' bold '))
button2.place(x=680, y=520)

button3 = Button(root, text="BACK", command=callOldScreen, width=10, bg="dark blue", fg="white",activebackground="#FF0000", activeforeground="white", font=('times', 15, ' bold '))
button3.place(x=500, y=520)

button4 = Button(root, text="Generate Documentation", command=click, width=20, bg="#27AE60", fg="white", activebackground="#1F618D", activeforeground="white", font=('times', 15, ' bold '))
button4.place(x=644, y=640)

button5 = Button(root, text="Show", command=show, width=10, bg="dark blue", fg="white",activebackground="#FF0000", activeforeground="white", font=('times', 15, ' bold '))
button5.place(x=680, y=710)


label=Label(root)
txt=scrolledtext.ScrolledText(label,width=150,height=10,background='#fff8dc', foreground='black')
txt.grid(row=1,column=0,rowspan=15,columnspan=17)
label.place(x=200,y=300)
txt.insert(INSERT,'\n CapblityID,\t\t DomainName,\t\t Organization ,\t\t poitofcontact,\t\t Address,\t\t contactNo,\t\t country,\t\tEmail,\t\t Description')


root.mainloop()