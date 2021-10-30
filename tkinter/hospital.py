from tkinter import *
import sqlite3
window=Tk()
window.title("DETAILS")
window.geometry("700x600")
window.config(bg='white')
a=Label(window,text="Total Number of Doctors",font=("bold",10)).place(x=10,y=10)
b=Label(window,text="Total Number of Nurses",font=("bold",10)).place(x=10,y=50)
c=Label(window,text="Total Number of Health Care Assistants",font=("bold",10)).place(x=10,y=90)
d=Label(window,text="Number of Beds in Covid 19 ward",font=("bold",10)).place(x=10,y=130)
e=Label(window,text="Number of Beds in Covid 19 ICU ward",font=("bold",10)).place(x=10,y=170)
f=Label(window,text="Total Number of Oxygen Cylinders",font=("bold",10)).place(x=10,y=210)
g=Label(window,text="Name of the person",font=("bold",10)).place(x=10,y=250)
h=Label(window,text="Date of Vaccination",font=("bold",10)).place(x=10,y=290)
i=Label(window,text="Aadhar Number",font=("bold",10)).place(x=10,y=330)
j=Label(window,text="Date of Birth",font=("bold",10)).place(x=10,y=370)
k=Label(window,text="Age",font=("bold",10)).place(x=10,y=410)
l=Label(window,text="Dosage Count",font=("bold",10)).place(x=10,y=450)
E1=Entry(window,width=20).place(x=270,y=10)
E2=Entry(window,width=20).place(x=270,y=50)
E3=Entry(window,width=20).place(x=270,y=90)
E4=Entry(window,width=20).place(x=270,y=130)
E5=Entry(window,width=20).place(x=270,y=170)
E6=Entry(window,width=20).place(x=270,y=210)
E7=Entry(window,width=20).place(x=270,y=250)
E8=Entry(window,width=20).place(x=270,y=290)
E9=Entry(window,width=20).place(x=270,y=330)
E10=Entry(window,width=20).place(x=270,y=370)
E11=Entry(window,width=20).place(x=270,y=410)
E12=Entry(window,width=20).place(x=270,y=450)

def add_data():
    db=sqlite3.connect("COVID-19.db")
    c=db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS READINESS_TABLE(no_of_doctors int,no_of nurses int,no_of_healthcareassistants int,no_of_beds int,no_of_bedsinICU int,no_of_oxygencylilnders int ,no_of_ventilators int)")
    c.execute("INSERT INTO READINESS_TABLE(no_of_doctors,no_of nurses,no_of_healthcareassistants,no_of_beds,no_of_bedsinICU,no_of_oxygencylilnders,no_of_ventilators) VALUES(?,?,?,?,?,?,?)",())
    c.execute("CREATE TABLE IF NOT EXISTS VACCINATION_TABLE(name text,date_of_vaccination text,aadhaar_no int,dob text,age int,Dosage_count int)")    
    db.commit()
    db.close()
    
    
Button(window,text="Submit",font=("bold",10),command=add_data).place(x=300,y=510)
window.mainloop()
