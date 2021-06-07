
import  tkinter as tk
from tkinter import *
import psycopg2

# connect to the database

con = psycopg2.connect(
    host='localhost',
    database='test',
    user='postgres',
    password='jayesh1')

# create a cursor
cur=con.cursor()

def addstudent():
    firstname = ent1.get()
    lastname = ent2.get()
    email = ent3.get()
    gender=ent4.get()
    dateofbirth=ent5.get()
    tenth=ent6.get()
    twelve=ent7.get()
    ug=ent8.get()
    pg=ent9.get()
    addrs=ent10.get()
    mobno=ent11.get()
    query ="INSERT INTO person(first_name, last_name, email,gender, date_of_birth, per10, per12, ug_cgpa, pg_cgpa, mobile1, addr) values(%s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s)"
    cur.execute(query, (firstname, lastname, email, gender,dateofbirth , tenth, twelve, ug, pg, mobno, addrs ))
    con.commit()
    print(firstname, lastname, email, gender, dateofbirth, tenth, twelve, ug, pg, mobno, addrs )
    print("Student is added")
    return True

win = Tk()

frm1 = Frame(win, width=100, highlightbackground='pink', highlightthicknes=4 )
#frm1.pack(side= tk.LEFT,padx=100)
frm1.grid(row=2,column=0, padx=20, pady=20, ipadx=20, ipady=20)
win.title("Created By Jayesh & Ritesh")
win.geometry("500x600")
#win.resizable(False, False)
win.configure(bg="#00ffff")
frm1['bg']="#C39BD3"

frm2 = Frame(win, width=5, highlightbackground='blue', highlightthicknes=4)
frm2['bg']="#C39BD3"
#frm2.pack(side=tk.LEFT, padx=100)
frm2.grid(row=1,column=0) 




var1 = StringVar()
firstname = StringVar()
var2 = StringVar()
lastname = StringVar()
var3 = StringVar()
email = StringVar()
var4 = StringVar()
gender = StringVar()
var5 = StringVar()
dateofbirth = StringVar()
var6 = StringVar()
tenthscore = StringVar()
var7 = StringVar()
twelvethscore = StringVar()
var8 = StringVar()
ugscore = StringVar()
var9 = StringVar()
pgscore = StringVar()
var10 = StringVar()
address = StringVar()
var11 = StringVar()
mobileno = StringVar()
var12=StringVar()
var13=StringVar()
var14=StringVar()


label1 = Label(frm1, textvariable = var1,bg="#C39BD3", font=15)
var1.set("First Name")
label1.grid(row=0, column=1)

ent1 = Entry (frm1, textvariable= firstname, font=15)
firstname.set("Enter first name")
ent1.grid(row=0, column=2)


label2 = Label(frm1, textvariable = var2,bg="#C39BD3", font=15)
var2.set("Last Name")
label2.grid(row=1, column=1)
ent2 = Entry (frm1, textvariable= lastname, font=15)
lastname.set("Enter last name")
ent2.grid(row=1, column=2)


label4 = Label(frm1, textvariable = var4,bg="#C39BD3", font=15)
var4.set("Gender")
label4.grid(row=3, column=1)
# Radiobutton(frm1, textvariable=gender, text=Male, value=gender)
ent4 = Entry (frm1, textvariable= gender, font=15)
gender.set("Enter Gender")
ent4.grid(row=3, column=2)

label5 = Label(frm1, textvariable = var5,bg="#C39BD3", font=15)
var5.set("Date of Birth")
label5.grid(row=4, column=1)
ent5 = Entry (frm1, textvariable= dateofbirth, font=15)
dateofbirth.set("YY-MM-DD")
ent5.grid(row=4, column=2)

label6 = Label(frm1, textvariable =var6,bg="#C39BD3", font=15)
var6.set("10th Percentage")
label6.grid(row=5, column=1)
ent6 = Entry (frm1, textvariable=tenthscore, font=15)
tenthscore.set("10th %")
ent6.grid(row=5, column=2)


label7 = Label(frm1, textvariable =var7,bg="#C39BD3", font=15)
var7.set("12th Percentage")
label7.grid(row=6, column=1)
ent7 = Entry (frm1, textvariable=twelvethscore, font=15)
twelvethscore.set("12th %")
ent7.grid(row=6, column=2)


label8 = Label(frm1, textvariable =var8,bg="#C39BD3", font=15)
var8.set("Graduation CGPA")
label8.grid(row=7, column=1)
ent8 = Entry (frm1, textvariable=ugscore, font=15)
ugscore.set("Enter CGPA")
ent8.grid(row=7, column=2)


label9 = Label(frm1, textvariable =var9,bg="#C39BD3", font=15)
var9.set("Post Graduation CGPA")
label9.grid(row=8, column=1)
ent9 = Entry (frm1, textvariable=pgscore, font=15)
pgscore.set("Enter CGPA")
ent9.grid(row=8, column=2)


label10 = Label(frm1, textvariable =var10,bg="#C39BD3", font=15)
var10.set("Address ")
label10.grid(row=9, column=1)
ent10 = Entry (frm1, textvariable=address, font=15)
address.set("Enter Address ")
ent10.grid(row=9, column=2)

label11 = Label(frm1, textvariable =var11,bg="#C39BD3", font=15)
var11.set("Mobile No. ")
label11.grid(row=10, column=1)
ent11 = Entry (frm1, textvariable=mobileno, font=15)
mobileno.set("Enter Mobile Number")
ent11.grid(row=10, column=2)

label3 = Label(frm1, textvariable = var3,bg="#C39BD3", font=15)
var3.set("E-mail")
label3.grid(row=11, column=1)
ent3 = Entry (frm1, textvariable= email, font=15)
email.set("Enter e-mail")
ent3.grid(row=11, column=2)

label12= Label(frm2, text= "Campus Recruitment Form" , font=25)
label12.grid(row=1, column=1)


btn1=Button(win, text="Submit", command=addstudent, font=16, bg='#F6CB38')
btn1.grid(row=3, column=1, padx=5, pady=5)

btn2=Button(win, text="Exit", command=win.quit , font=16,bg='#F6CB38' )
btn2.grid(row=3, column=2,padx=5, pady=5 )



win.mainloop()
#close the cursor
cur.close()

# close the connection
con.close()

