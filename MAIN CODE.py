from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from fpdf import FPDF
import pickle
import datetime
import math

#initializing variables
customer_ID=0
dictionary={}
Order = {}
customer_name=""
cashier_name =""


#defining functions
def info(l):    
    pdf.set_font('times', 'I', 13)
    for i in range(len(l)):
        pdf.multi_cell(190, 5, l[i], border=0, ln=1, align="C")


def display():
    f = open("billing.dat", 'rb')
    try:
        while True:
            data = pickle.load(f)
    except EOFError:
        f.close()
    return data


'''def createdatabase():
    mycursor.execute("CREATE DATABASE Project")'''


def addtable():
    mycursor.execute("CREATE TABLE Customers (ID integer(225), NAME VARCHAR(25), MOBILE_NUMBER VARCHAR(12), CASHIER VARCHAR(15), DATEandTIME VARCHAR(30) ) )")


def addcontent(id,name,number,cashier,datetime):

    sqlFormula = "Insert into Customers value({},'{}','{}','{}','{}')".format(id,name,number,cashier,datetime)
    mycursor.execute(sqlFormula)
    mydb.commit()


def filemaker(d):
    for food in d:
        if d[food][0] == 0:
            pass
        else:
            Order[food] = d[food]

    with open("Billing.dat", "wb") as bill:
        pickle.dump(Order, bill)
        bill.flush()


def ordering():
    global dictionary, Order, customer_name, customer_number, cashier_name
    dictionary = {"Mango":[mango.get(),40,mango.get()*40],
                  "Vanilla":[vanilla.get(),35,vanilla.get()*35],
                  "Chocolate":[chocolate.get(),45,45*chocolate.get()],
                  "Butterscotch":[butterscotch.get(),35,35*butterscotch.get()],
                  "Pista": [pista.get(),35,35*pista.get()],
                  "Strawberry": [strawberry.get(),30,30*strawberry.get()],
                  "Mintchip": [mintchip.get(),30,30*mintchip.get()],
                  "Oreo": [oreo.get(),45,45*oreo.get()],
                  "Cassata": [cassata.get(),35,35*cassata.get()],
                  "Samosa":[samosa.get(),30,30*samosa.get()],
                  "Bhelpuri":[bp.get(),30,30*bp.get()],
                  "Dhaipuri": [dp.get(),35,30*dp.get()],
                  "Sevpuri":[sp.get(),30,30*sp.get()],
                  "Panipuri":[pp.get(),30,30*pp.get()],
                  "Masalpuri":[mp.get(),30,30*mp.get()]
                  }
    messagebox.showinfo(title="MESSAGE",message="YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
    filemaker((dictionary))
    customer_name = name.get()
    cashier_name = cashier.get()
    customer_number = ph.get()

window = Tk()
window.title("BILLING SOFTWARE")
window.geometry("1080x1000")
notebook = ttk.Notebook(window)


tab1 = Frame(notebook,bg="light blue")
tab2 = Frame(notebook,bg="light blue")
notebook.add(tab1,text="page1")
notebook.add(tab2,text="page2")
notebook.pack(expand=True,fill="both")

#-----------------------------------------------------------------------------------------------------------------------

#creating the products and adding to the screen 15 items upto line 400
mangoframe= Frame(tab1,bg="#f5f59d",height=225,width=350)
mangoframe.grid(row=0,column=0,pady=5,padx=50,sticky="nsew")
mangoframe.pack_propagate(0)

Mango = PhotoImage(file="mango.png")
mangoimage = Label(mangoframe,
                   image=Mango,
                   compound="top",
                   text="MANGO ICECREAM RS 40",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
mangoimage.pack(side="top")

mango_count = Label(mangoframe,text="Quantity of Mango scoops:",bg="white").pack(side="left")

mango = IntVar()

for i in range(5):
    radiobutton = Radiobutton(mangoframe, text=i, variable=mango, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
vanillaframe= Frame(tab1,bg="#f5f59d",height=225,width=350)
vanillaframe.grid(row=1,column=0,pady=5,padx=50,sticky="nsew")
vanillaframe.pack_propagate(0)

Vanilla = PhotoImage(file="vanilla.png")
vanillaimage = Label(vanillaframe,
                   image=Vanilla,
                   compound="top",
                   text="VANILLA ICECREAM RS 35",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
vanillaimage.pack(side="top")

vanilla_count = Label(vanillaframe,text="Quantity of Vanilla scoops:",bg="white").pack(side="left")

vanilla = IntVar()

for i in range(5):
    radiobutton = Radiobutton(vanillaframe, text=i, variable=vanilla, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
chocolateframe= Frame(tab1,bg="#f5f59d",height=225,width=350)
chocolateframe.grid(row=2,column=0,pady=5,padx=50,sticky="nsew")
chocolateframe.pack_propagate(0)

Chocolate = PhotoImage(file="chocolate.png")
chocolateimage = Label(chocolateframe,
                   image=Chocolate,
                   compound="top",
                   text="CHOCOLATE ICECREAM RS 45",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
chocolateimage.pack(side="top")

chocolate_count = Label(chocolateframe,text="Quantity of Chocolate scoops:",bg="white").pack(side="left")

chocolate = IntVar()

for i in range(5):
    radiobutton = Radiobutton(chocolateframe, text=i, variable=chocolate, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
butterscotchframe= Frame(tab1,bg="#f5f59d",height=225,width=350)
butterscotchframe.grid(row=0,column=1,pady=5,padx=50,sticky="nsew")
butterscotchframe.pack_propagate(0)

Butterscotch = PhotoImage(file="butterscotch.png")
butterscotchimage = Label(butterscotchframe,
                   image=Butterscotch,
                   compound="top",
                   text="BUTTERSCOTCH ICECREAM RS 35",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
butterscotchimage.pack(side="top")

butterscotch_count = Label(butterscotchframe,text="Quantity of Butterscotch scoops:",bg="white").pack(side="left")

butterscotch = IntVar()

for i in range(5):
    radiobutton = Radiobutton(butterscotchframe, text=i, variable=butterscotch, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
pistaframe= Frame(tab1,bg="#f5f59d",height=225,width=350)
pistaframe.grid(row=1,column=1,pady=5,padx=50,sticky="nsew")
pistaframe.pack_propagate(0)

Pista = PhotoImage(file="pista.png")
pistaimage = Label(pistaframe,
                   image=Pista,
                   compound="top",
                   text="PISTA ICECREAM RS 35",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
pistaimage.pack(side="top")

pista_count = Label(pistaframe,text="Quantity of Pista scoops:",bg="white").pack(side="left")

pista = IntVar()

for i in range(5):
    radiobutton = Radiobutton(pistaframe, text=i, variable=pista, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
strawberryframe= Frame(tab1,bg="#f5f59d",height=225,width=350)
strawberryframe.grid(row=2,column=1,pady=5,padx=50,sticky="nsew")
strawberryframe.pack_propagate(0)

Strawbery = PhotoImage(file="strawberry.png")
strawberryimage = Label(strawberryframe,
                   image=Strawbery,
                   compound="top",
                   text="STRAWBERRY ICECREAM RS 30",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
strawberryimage.pack(side="top")

strawberry_count = Label(strawberryframe,text="Quantity of Strawberry scoops:",bg="white").pack(side="left")

strawberry = IntVar()

for i in range(5):
    radiobutton = Radiobutton(strawberryframe, text=i, variable=strawberry, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
mintchipframe= Frame(tab1,bg="#f5f59d",height=225,width=350)
mintchipframe.grid(row=0,column=2,pady=5,padx=50,sticky="nsew")
mintchipframe.pack_propagate(0)

Mintchip = PhotoImage(file="mintchip.png")
mintchipimage = Label(mintchipframe,
                   image=Mintchip,
                   compound="top",
                   text="MINT CHIP ICECREAM RS 30",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
mintchipimage.pack(side="top")

mintchip_count = Label(mintchipframe,text="Quantity of MintChip scoops:",bg="white").pack(side="left")

mintchip = IntVar()

for i in range(5):
    radiobutton = Radiobutton(mintchipframe, text=i, variable=mintchip, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
oreoframe= Frame(tab1,bg="#f5f59d",height=225,width=350)
oreoframe.grid(row=1,column=2,pady=5,padx=50,sticky="nsew")
oreoframe.pack_propagate(0)

Oreo = PhotoImage(file="oreo.png")
oreoimage = Label(oreoframe,
                   image=Oreo,
                   compound="top",
                   text="OREO ICECREAM RS 45",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
oreoimage.pack(side="top")

oreo_count = Label(oreoframe,text="Quantity of Oreo scoops:",bg="white").pack(side="left")

oreo = IntVar()

for i in range(5):
    radiobutton = Radiobutton(oreoframe, text=i, variable=oreo, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
cassataframe= Frame(tab1,bg="#f5f59d",height=225,width=350)
cassataframe.grid(row=2,column=2,pady=5,padx=50,sticky="nsew")
cassataframe.pack_propagate(0)

Cassata = PhotoImage(file="cassata.png")
cassataimage = Label(cassataframe,
                   image=Cassata,
                   compound="top",
                   text="CASSATA ICECREAM RS 35",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
cassataimage.pack(side="top")

cassata_count = Label(cassataframe,text="Quantity of Cassata scoops:",bg="white").pack(side="left")

cassata = IntVar()

for i in range(5):
    radiobutton = Radiobutton(cassataframe, text=i, variable=cassata, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
contents = [mangoframe,vanillaframe,chocolateframe,butterscotchframe,
            pistaframe,strawberryframe,mintchipframe,oreoframe,cassataframe]

row_number = 0
for frame in contents:
    Grid.rowconfigure(tab1,row_number,weight=1)
    Grid.columnconfigure(tab1,row_number,weight=1)
    row_number+=1
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
samosaframe= Frame(tab2,bg="#f5f59d",height=225,width=350)
samosaframe.grid(row=0,column=0,pady=5,padx=50,sticky="nsew")
samosaframe.pack_propagate(0)

Samosa = PhotoImage(file="samosa.png")
samosaimage = Label(samosaframe,
                   image=Samosa,
                   compound="top",
                   text="Samosa RS 30",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
samosaimage.pack(side="top")

samosa_count = Label(samosaframe,text="Quantity of samosas:",bg="white").pack(side="left")

samosa = IntVar()

for i in range(5):
    radiobutton = Radiobutton(samosaframe, text=i, variable=samosa, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
bpframe= Frame(tab2,bg="#f5f59d",height=225,width=350)
bpframe.grid(row=1,column=0,pady=5,padx=50,sticky="nsew")
bpframe.pack_propagate(0)

Bp = PhotoImage(file="bhelpuri.png")
bpimage = Label(bpframe,
                   image=Bp,
                   compound="top",
                   text="BHEL PURI RS 30",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
bpimage.pack(side="top")

bp_count = Label(bpframe,text="Quantity of Bhel puri:",bg="white").pack(side="left")

bp = IntVar()

for i in range(5):
    radiobutton = Radiobutton(bpframe, text=i, variable=bp, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
dpframe= Frame(tab2,bg="#f5f59d",height=225,width=350)
dpframe.grid(row=0,column=1,pady=5,padx=50,sticky="nsew")
dpframe.pack_propagate(0)

Dp = PhotoImage(file="dhaipuri.png")
dpimage = Label(dpframe,
                   image=Dp,
                   compound="top",
                   text="DHAI PURI RS 35",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
dpimage.pack(side="top")

dp_count = Label(dpframe,text="Quantity of Dhai puri:",bg="white").pack(side="left")

dp = IntVar()

for i in range(5):
    radiobutton = Radiobutton(dpframe, text=i, variable=dp, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
spframe= Frame(tab2,bg="#f5f59d",height=225,width=350)
spframe.grid(row=1,column=1,pady=5,padx=50,sticky="nsew")
spframe.pack_propagate(0)

Sp = PhotoImage(file="sevpuri.png")
spimage = Label(spframe,
                   image=Sp,
                   compound="top",
                   text="SEV PURI RS 30",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
spimage.pack(side="top")

sp_count = Label(spframe,text="Quantity of Sev puri:",bg="white").pack(side="left")

sp = IntVar()

for i in range(5):
    radiobutton = Radiobutton(spframe, text=i, variable=sp, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
ppframe= Frame(tab2,bg="#f5f59d",height=225,width=350)
ppframe.grid(row=0,column=2,pady=5,padx=50,sticky="nsew")
ppframe.pack_propagate(0)

Pp = PhotoImage(file="panipuri.png")
ppimage = Label(ppframe,
                   image=Pp,
                   compound="top",
                   text="PANI PURI RS 30",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
ppimage.pack(side="top")

pp_count = Label(ppframe,text="Quantity of Pani puri:",bg="white").pack(side="left")

pp = IntVar()

for i in range(5):
    radiobutton = Radiobutton(ppframe, text=i, variable=pp, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
mpframe= Frame(tab2,bg="#f5f59d",height=225,width=350)
mpframe.grid(row=1,column=2,pady=5,padx=50,sticky="nsew")
mpframe.pack_propagate(0)

Mp = PhotoImage(file="masalpuri.png")
mpimage = Label(mpframe,
                   image=Mp,
                   compound="top",
                   text="MASAL PURI RS 30",
                   fg="black",
                   bg="#f5f59d",
                   font=("bold"))
mpimage.pack(side="top")

mp_count = Label(mpframe,text="Quantity of Masal puri:",bg="white").pack(side="left")

mp = IntVar()

for i in range(5):
    radiobutton = Radiobutton(mpframe, text=i, variable=mp, value=i)
    radiobutton.pack(side="left")
#-----------------------------------------------------------------------------------------------------------------------
contents2=[samosaframe,bpframe,dpframe,spframe,ppframe,mpframe]
row_num = 0
for frame in contents2:
    Grid.rowconfigure(tab2,row_num,weight=1)
    Grid.columnconfigure(tab2,row_num,weight=1)
    row_num+=1
#-----------------------------------------------------------------------------------------------------------------------
#customer and cashier info
formframe = Frame(tab2,bg="#f5f59d",height=150,width=350)
formframe.grid(row=2,column=0)
formframe.pack_propagate(0)

#extracting phone number , name , cashier name
ph = Entry(formframe,width=20,fg="Blue")
ph.grid(row=0,column=1,padx=10,pady=10)

lab1 = Label(formframe,text="Enter your number here (+91):",fg="Blue")
lab1.grid(row=0,column=0,padx=10,pady=10)

name = Entry(formframe,width=20,fg="Blue")
name.grid(row=1,column=1,padx=10,pady=10)

lab2 = Label(formframe,text="Enter your name here: ",fg="Blue")
lab2.grid(row=1,column=0,padx=10,pady=10)

submitbutton = Button(tab2, font="AIRAL", text="Click here to place order: ", command=ordering, width=20)
submitbutton.grid(row=2,column=2)


cashierframe = Frame(tab2,bg="#f5f59d",height=150,width=350)
cashierframe.grid(row=2,column=1)

cashierlab = Label(cashierframe,text="SELECT CASHIER NAME: ",padx=10,pady=10,font="AIRAL")
cashierlab.pack(side="top")

cashier = StringVar()
cashiers = ["Aditya N","Manas","Pranav"]
for employee in cashiers:
    radiobutton = Radiobutton(cashierframe,text=employee,variable=cashier,value=employee,font="ARIAL")
    radiobutton.pack(side="left",padx=5,pady=8)
#-----------------------------------------------------------------------------------------------------------------------
customer_name = name.get()
cashier_name = cashier.get()
customer_number = ph.get()
window.mainloop()


#-----------------------------------------------------------------------------------------------------------------------
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()

# shop name
shop = "Snacks Point"
pdf.set_font("helvetica", "BIU", 45)
pdf.cell(0, 30, shop, ln=1, align="C", border=0)


website = "website : www.snackspoint.co.in"
phone = "Phone no : 5842 8756"
address = [
    'Address : No.532, 10th Main 36th Cross Road, next to Namdharis 5th Block, Jayanagar Bengaluru, Karnataka-560041']
details = address + [website] + [phone]

info(details)
pdf.cell(0, 4, '-' * 124, ln=1, border=0)

# Bill number

f = open('Bill counter.txt', 'r')
content = f.read()
f.close()
bno = int(content)

f = open('Bill counter.txt', 'w')
content = str(bno + 1)
f.write(content)
f.close()

# General details



pdf.set_font("helvetica", "I", 15)
pdf.cell(0, 7, "Bill number           : " + str(bno), ln=1, border=0)
pdf.cell(0, 7, "Customer name   : " + customer_name , ln=1, border=0)
pdf.cell(0, 7, "Cashier                : " + cashier_name, ln=1, border=0)
time = datetime.datetime.now()
pdf.multi_cell(0, 7, time.strftime("Date                    : %d-%m-%y \nTime                   : %H : %M : %S"),
               ln=1, border=0)

pdf.set_font("helvetica", "I", 13)
pdf.cell(0, 4, '-' * 124, ln=1, border=0)

# bill headings

pdf.set_font("helvetica", "B", 20)
pdf.cell(94, 13, "Items", border=0, ln=0)
pdf.cell(32, 13, "Quantity", border=0, ln=0)
pdf.cell(32, 13, "Rate", border=0, ln=0, align="C")
pdf.cell(32, 13, "Price", border=0, ln=1, align="C")

# contents of bill
pdf.set_font("courier", "", 18)

# dictionary
d = display()
total = 0
for i in d.keys():
    pdf.cell(94, 10, i, border=0, ln=0)
    pdf.cell(32, 10, str(d[i][0]), border=0, ln=0, align="C")
    pdf.cell(32, 10, str(d[i][1]), border=0, ln=0, align="C")
    pdf.cell(32, 10, str(d[i][2]), border=0, ln=1, align="C")
    total += d[i][2]

pdf.set_font("helvetica", "I", 13)
pdf.cell(0, 4, '-' * 124, ln=1, border=0)

# cost calculation
tas = round(total * 0.18,2)
gtotal = total + tas
pdf.set_font("courier", "", 20)
pdf.cell(140, 7, "Total Rs        : ", border=0, ln=0)
pdf.cell(50, 7, str(total), border=0, ln=1, align="R")
pdf.cell(140, 7, "CGST 9%         : ", border=0, ln=0)
pdf.cell(50, 7, str(tas / 2), border=0, ln=1, align="R")
pdf.cell(140, 7, "SGST 9%         : ", border=0, ln=0)
pdf.cell(50, 7, str(tas / 2), border=0, ln=1, align="R")
pdf.cell(140, 7, "Grand Total Rs  : ", border=0, ln=0)
pdf.cell(50, 7, str(gtotal), border=0, ln=1, align="R")

# Ending
pdf.set_font('times', 'I', 13)
pdf.cell(0, 4, '-' * 124, ln=1, border=0)
pdf.cell(0, 5, "thank you " + customer_name + '!! ' + "Do visit us again", border=0, ln=1, align="C")
pdf.cell(0, 5, '~ ~ ' * 3, border=0, ln=1, align="C")

bname = "Bill" + str(bno)

pdf.output(bname + '.pdf')
#-----------------------------------------------------------------------------------------------------------------------
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password="onepiece@09",
    database="project"
)
mycursor = mydb.cursor()
customer_ID = bno
idk = str(datetime.datetime.now())
DAT = idk[0:19]
addcontent(customer_ID,customer_name,customer_number,cashier_name,DAT)
