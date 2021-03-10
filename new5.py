from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import re
from docx import Document
import os
from PIL import ImageTk, Image


root = Tk()
root.title("Compliance Login")
root.geometry("1600x799")
# root.wm_attributes('-transparentcolor','green')
# root.configure(background='black')
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
my_canvas.config(yscrollcommand=scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
second_frame = Frame(my_canvas)
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")


def clearAllFields():
    CapabilityIDvalue.set("")
    DomainNamevalue.set("")
    OrganizationNamevalue.set("")
    PointofContactvalue.set("")
    OrganizationAddressvalue.set("")
    ContactNumbervalue.set("")

def validate_phoneno(user_phoneno):
    if user_phoneno.isdigit():
        return True
    elif user_phoneno == "":
        return True
    else:
        messagebox.showinfo("information", 'only digit are allowed for phone number')
        return False

def callNewScreen():
    root.destroy();
    os.system("python sal.py")

CapabilityIDvalue = StringVar()
DomainNamevalue = StringVar()
OrganizationNamevalue = StringVar()
PointofContactvalue = StringVar()
OrganizationAddressvalue = StringVar()
ContactNumbervalue = StringVar()


def database():
    global CapabilityIDvalue
    global DomainNamevalue
    global OrganizationNamevalue
    global PointofContactvalue
    global OrganizationAddressvalue
    global ContactNumbervalue
    CapabilityIDvalue = CapabilityIDvalue.get()
    DomainNamevalue = DomainNamevalue.get()
    OrganizationNamevalue = OrganizationNamevalue.get()
    PointofContactvalue = PointofContactvalue.get()
    OrganizationAddressvalue = OrganizationAddressvalue.get()
    ContactNumbervalue = ContactNumbervalue.get()
    conn = mysql.connector.connect(host="localhost", user="root", passwd="Zaroon@786", database="sakila",auth_plugin="mysql_native_password")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO member4(CapabilityID, DomainName, OrganizationName, PointofContact, OrganizationAddress, ContactNumber) VALUES(%s,%s,%s,%s,%s,%s)',(CapabilityIDvalue, DomainNamevalue, OrganizationNamevalue, PointofContactvalue, OrganizationAddressvalue,ContactNumbervalue))
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    print("Query Executed successfully")
    conn.commit()



def getvals():

    print("Submitting form")
    print(f"{CapabilityIDvalue.get(), DomainNamevalue.get(), OrganizationNamevalue.get(), PointofContactvalue.get(), OrganizationAddressvalue.get(), ContactNumbervalue.get()} ")

    with open("records.txt", "w+") as f:
        f.write(f"\r\n\t\t\t\t COMPLIANCE ASSESSMENT REPORT" "\r\n")
        f.write(f"\r\nCapability ID: " + CapabilityIDvalue.get() + "\r\n")
        f.write(f"\r\nDomain Name: " + DomainNamevalue.get() + "\r\n")
        f.write(f"\r\nOrganization Name: " + OrganizationNamevalue.get() + "\r\n")
        f.write(f"\r\nPoint of Contact: " + PointofContactvalue.get() + "\r\n")
        f.write(f"\r\nOrganization Address: " + OrganizationAddressvalue.get() + "\r\n")
        f.write(f"\r\nContact Number: " + ContactNumbervalue.get() + "\r\n")


canv = Canvas(master=root)
canv.place(x=0, y=0, width=1600, height=799)

img = ImageTk.PhotoImage(Image.open("greeeen.jpg"))  # <-- PIL
canv.create_image(0, 0, image=img, anchor='nw')


# Heading
label=Label(root, text="XentIT FedRAMP & CMMC Compliance", bg="black", fg="orange", width=45, height=2,font=('comicsansms', 30, 'italic bold underline'))
label.place(x=200, y=20)

# Text for our form
CapabilityID = Label(root, text="Capability ID", width=20, height=1, fg="black", bg="white",font=('times', 15, ' bold '))
DomainName = Label(root, text="Domain Name", width=20, height=1, fg="black", bg="white",font=('times', 15, ' bold '))
OrganizationName = Label(root, text="Organization Name", width=20, height=1, fg="black", bg="white",font=('times', 15, ' bold '))
PointofContact = Label(root, text="Point of Contact", width=20, height=1, fg="black", bg="white",font=('times', 15, ' bold '))
OrganizationAddress = Label(root, text="Organization Address", width=20, height=1, fg="black", bg="white",font=('times', 15, ' bold '))
ContactNumber = Label(root, text="Contact Number", width=20, height=1, fg="black", bg="white",font=('times', 15, ' bold '))

CapabilityID.place(x=380, y=150)
DomainName.place(x=380, y=200)
OrganizationName.place(x=380, y=250)
PointofContact.place(x=380, y=300)
OrganizationAddress.place(x=380, y=350)
ContactNumber.place(x=380, y=400)


# Entries for our form
txt = Entry(root, textvariable=CapabilityIDvalue, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
txt2 = Entry(root, textvariable=DomainNamevalue, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
txt3 = Entry(root, textvariable=OrganizationNamevalue, width=20, bg="white", fg="black",font=('times', 15, ' bold '))
txt4 = Entry(root, textvariable=PointofContactvalue, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
txt5 = Entry(root, textvariable=OrganizationAddressvalue, width=20, bg="white", fg="black",font=('times', 15, ' bold '))
txt6 = Entry(root, textvariable=ContactNumbervalue, width=20, bg="white", fg="black", font=('times', 15, ' bold '))

# Packing the Entries
txt.place(x=900, y=150)
txt2.place(x=900, y=200)
txt3.place(x=900, y=250)
txt4.place(x=900, y=300)
txt5.place(x=900, y=350)
txt6.place(x=900, y=400)
valid_phoneno = root.register(validate_phoneno)
txt6.config(validate="key", validatecommand=(valid_phoneno, '%P'))

Button(text="Proceed", command=callNewScreen, width=10, bg="dark blue", fg="white", activebackground="#1F618D",activeforeground="white", font=('times', 15, ' bold ')).place(x=850, y=520)
button = Button(root, text="CLEAR", command=clearAllFields, width=10, bg="dark blue", fg="white",activebackground="#27AE60", activeforeground="white", font=('times', 15, ' bold ')).place(x=500,y=520)
Button = Button(root, text="SAVE", command=lambda: [getvals(),database()], width=10, bg="dark blue",fg="white",activebackground="#27AE60", activeforeground="white", font=('times', 15, ' bold ')).place(x=680,y=520)

root.mainloop()