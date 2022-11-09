import tkinter as tk
from tkinter import *
from PIL import ImageTk
import mysql.connector
import datetime as d
from tkinter import messagebox, ttk
root = Tk()
root.geometry("1300x760")
root.title("Food Ordering System")
###############################----------FRAME---------------------------------------------############################################
framelog = Frame(root, bg="purple", relief=RIDGE, bd=5)
framelog.place(x=1100, y=20, height=70, width=150)
title1 = Label(framelog, text="Menu", font=("ariel", 35, "bold"), fg="#d77337", bg="pink").place(x=10, y=0)

table1 = Frame(root, width=200, height=360, bd=10, relief="raised", bg="firebrick1").place(x=760, y=100)
table2 = Frame(root, width=200, height=360, bd=10, relief="raised", bg="royal blue").place(x=960, y=100)
table3 = Frame(root, width=200, height=360, bd=10, relief="raised", bg="sandy brown").place(x=1160, y=100)
table4 = Frame(root, width=170, height=360, bd=10, relief="raised", bg="violetRed1").place(x=1360, y=100)
table5 = Frame(root, width=770, height=135, bd=10, relief=RAISED, bg="gray64").place(x=760, y=460)
table6=Frame(root, bd=10,height=400, relief=RAISED, bg="gray64")
table6.place(x=0,y=600)

framelog2 = Frame(root, bg="purple", relief=RIDGE, bd=5)
framelog2.place(x=100, y=20, height=70, width=520)
title2 = Label(framelog2, text="Customer Information", font=("ariel", 35, "bold"), fg="#d77337", bg="pink").place(x=10, y=0)
Infoframe = Frame(root, width=759, height=500, bd=10, relief="raised").place(x=0, y=100)
#-----------------------------------------------------------------------------------------------------------------------#
name_of_cust=StringVar()
mobile_of_cust=IntVar()
amount_total=IntVar()
order_num_of_cust=IntVar()
Prefernce_of_cust=StringVar()
date2=d.datetime.now()


#-------------------------------------------CUSTOMER INFORMATION--------------------------------------------------------#
customername = Label(Infoframe, text="Customer Name", font=("italic", 16, "bold")).place(x=10, y=110)
txt_cname = Entry(Infoframe,textvariable=name_of_cust, font=("times new roman", 15))
txt_cname.place(x=280, y=118, width=290, height=20)

customermobile = Label(Infoframe, text="Customer Mobile Number", font=("italic", 16, "bold")).place(x=10, y=170)
txt_mobnum = Entry(Infoframe,textvariable=mobile_of_cust, font=("times new roman", 15))
txt_mobnum.place(x=280, y=170, width=290, height=20)

Orderlabel = ttk.Label(text="Order Number:", font=("italic", 16, "bold")).place(x=20, y=340)
orderlabel1=Entry(Infoframe,textvariable=order_num_of_cust, width=20)
orderlabel1.place(x=280,y=340)
# ------------------------------------------------------------------------------------------------------------------------------------------#
# ========================================< CASH PAYMENT METHOD + PREFERENCE >=============================================================#
# ------------------------------------------------------------------------------------------------------------------------------------------#
MOP = ttk.Label(text="Mode of Payment:", font=("italic", 16, "bold")).place(x=20, y=230)
Preferencelabel = ttk.Label(text="Preference:", font=("italic", 16, "bold")).place(x=20, y=290)
MOC = tk.StringVar()
Preference1 = tk.StringVar()
n1 = ttk.Combobox(root, textvariable=MOC)               #MOC- MODE OF CASH
n2 = ttk.Combobox(root, textvariable=Preference1)
n1['values'] = ['cash', 'debit', 'credit']
n2['values'] = ['Take away', 'Dine In']
n2['state'] = 'readonly'
n2.place(x=280, y=290)
# prevent typing a value
n1['state'] = 'readonly'
# place the widget
n1.place(x=280, y=230)
#---------------------------------------------------------------------------------------------------------------------------------------------#
def ResetFunction():
    orderlabel1.delete(0,END)
    txt_cname.delete(0,END)
    txt_mobnum.delete(0,END)
    n1.set(0)
    n2.set(0)
    VarCB.set('0')
    VarNG.set("0")
    VarVG.set("0")
    VarSB.set("0")
    VarVZ.set("0")
    VarNZ.set("0")
    VarCP.set("0")
    VarFP.set("0")
    VarAP.set("0")
    VarGP.set("0")
    VarPO.set("0")
    VarSW.set("0")
    VarSM.set("0")
    VarBT.set("0")
    VarEO.set("0")
    VarMG.set("0")
    VarPV.set("0")
    VarCBR.set("0")
    VarVT.set("0")
    VarNT.set("0")
    VarRC.set("0")
    VarRO.set("0")
    VarDM.set("0")
    VarMV.set("0")
    VarKU.set("0")
    VarSP.set("0")
    VarTE.set("0")
    VarCF.set("0")
    VarCO.set("0")
    VarCL.set("0")
    VarIC.set("0")
    VarGJ.set("0")
    VarKUL.set("0")
    VarLSSI.set("0")
    txtCB.config(state=DISABLED)
    txtNG.config(state=DISABLED)
    txtVG.config(state=DISABLED)
    txtSB.config(state=DISABLED)
    txtVZ.config(state=DISABLED)
    txtNZ.config(state=DISABLED)
    txtCP.config(state=DISABLED)
    txtFP.config(state=DISABLED)
    txtAP.config(state=DISABLED)
    txtGP.config(state=DISABLED)
    txtPO.config(state=DISABLED)
    txtSW.config(state=DISABLED)
    txtSMSA.config(state=DISABLED)
    txtBUTO.config(state=DISABLED)
    txtEO.config(state=DISABLED)
    txtMG.config(state=DISABLED)
    txtPV.config(state=DISABLED)
    txtCBR.config(state=DISABLED)
    txtVT.config(state=DISABLED)
    txtNT.config(state=DISABLED)
    txtRC.config(state=DISABLED)
    txtRO.config(state=DISABLED)
    txtDM.config(state=DISABLED)
    txtMV.config(state=DISABLED)
    txtKU.config(state=DISABLED)
    txtSP.config(state=DISABLED)
    txtTE.config(state=DISABLED)
    txtCF.config(state=DISABLED)
    txtCO.config(state=DISABLED)
    txtCL.config(state=DISABLED)
    txtIC.config(state=DISABLED)
    txtRG.config(state=DISABLED)
    txtKUL.config(state=DISABLED)
    txtLSSI.config(state=DISABLED)
    a1.set(0)
    a2.set(0)
    a3.set(0)
    a4.set(0)
    b1.set(0)
    b2.set(0)
    b3.set(0)
    b4.set(0)
    c1.set(0)
    c2.set(0)
    c3.set(0)
    c4.set(0)
    c5.set(0)
    c6.set(0)
    c7.set(0)
    c8.set(0)
    c9.set(0)
    d1.set(0)
    d2.set(0)
    d3.set(0)
    d4.set(0)
    d5.set(0)
    d6.set(0)
    d7.set(0)
    d8.set(0)
    d9.set(0)
    e1.set(0)
    e2.set(0)
    e3.set(0)
    e4.set(0)
    e5.set(0)
    e6.set(0)
    e7.set(0)
    e8.set(0)

    Vartotbutton.set(0)
    VarChangeLabel.set(0)
    Varinput.set(0)
    EnterAmount1.delete(0,END)

def Cheesea1():
    if a1.get() == 1:
        txtCB.config(state=NORMAL)
        VarCB.set("")
    elif a1.get() == 0:
        txtCB.config(state=DISABLED)
        VarCB.set("0")
def Nonveg2():
    if a2.get() == 1:
        txtNG.config(state=NORMAL)
        VarNG.set("")
    elif a2.get() == 0:
        txtNG.config(state=DISABLED)
        VarNG.set("0")
def CrispyVeg1():
    if a3.get() == 1:
        txtVG.config(state=NORMAL)
        VarVG.set("")
    elif a3.get() == 0:
        txtVG.config(state=DISABLED)
        VarVG.set("0")
def Pizzaburger1():
    if a4.get() == 1:
        txtSB.config(state=NORMAL)
        VarSB.set("")
    elif a4.get() == 0:
        txtSB.config(state=DISABLED)
        VarSB.set("0")
#-----------------------------------------------------------------------------#
def VegPizza1():
    if b1.get() == 1:
        txtVZ.config(state=NORMAL)
        VarVZ.set("")
    elif b1.get() == 0:
        txtVZ.config(state=DISABLED)
        VarVZ.set("0")
def NonvegPizza1():
    if b2.get() == 1:
        txtNZ.config(state=NORMAL)
        VarNZ.set("")
    elif b2.get() == 0:
        txtNZ.config(state=DISABLED)
        VarNZ.set("0")
def Cheesepizza1():
    if b3.get() == 1:
        txtCP.config(state=NORMAL)
        VarCP.set("")
    elif b3.get() == 0:
        txtCP.config(state=DISABLED)
        VarCP.set("0")
def Farmhouse1():
    if b4.get() == 1:
        txtFP.config(state=NORMAL)
        VarFP.set("")
    elif b4.get() == 0:
        txtFP.config(state=DISABLED)
        VarFP.set("0")
#-----------------------------------------------------------------------------#
def Aloo1():
    if c1.get() == 1:
        txtAP.config(state=NORMAL)
        VarAP.set("")
    elif c1.get() == 0:
        txtAP.config(state=DISABLED)
        VarAP.set("0")

def Gobi1():
    if c2.get() == 1:
        txtGP.config(state=NORMAL)
        VarGP.set("")
    elif c2.get() == 0:
        txtGP.config(state=DISABLED)
        VarGP.set("0")
def Poha1():
    if c3.get() == 1:
        txtPO.config(state=NORMAL)
        VarPO.set("")
    elif c3.get() == 0:
        txtPO.config(state=DISABLED)
        VarPO.set("0")
def VegSandwich1():
    if c4.get() == 1:
        txtSW.config(state=NORMAL)
        VarSW.set("")
    elif c4.get() == 0:
        txtSW.config(state=DISABLED)
        VarSW.set("0")

def Samosa1():
    if c5.get() == 1:
        txtSMSA.config(state=NORMAL)
        VarSM.set("")
    elif c5.get() == 0:
        txtSMSA.config(state=DISABLED)
        VarSM.set("0")
def ButterToast1():
    if c6.get() == 1:
        txtBUTO.config(state=NORMAL)
        VarBT.set("")
    elif c6.get() == 0:
        txtBUTO.config(state=DISABLED)
        VarBT.set("0")
def Omelet1():
    if c7.get() == 1:
        txtEO.config(state=NORMAL)
        VarEO.set("")
    elif c7.get() == 0:
        txtEO.config(state=DISABLED)
        VarEO.set("0")

def MasalaMaggi1():
    if c8.get() == 1:
        txtMG.config(state=NORMAL)
        VarMG.set("")
    elif c8.get() == 0:
        txtMV.config(state=DISABLED)
        VarMG.set("0")

def PAVBHAJI1():
    if c9.get() == 1:
        txtPV.config(state=NORMAL)
        VarPV.set("")
    elif c9.get() == 0:
        txtPV.config(state=DISABLED)
        VarPV.set("0")

#------------------------------------------------------------------------------#
def Cholebhature1():
    if d1.get() == 1:
        txtCBR.config(state=NORMAL)
        VarCBR.set("")
    elif d1.get() == 0:
        txtCBR.config(state=DISABLED)
        VarCBR.set("0")
def VegThali1():
    if d2.get() == 1:
        txtVT.config(state=NORMAL)
        VarVT.set("")
    elif d2.get() == 0:
        txtVT.config(state=DISABLED)
        VarVT.set("0")
def NonVegThali1():
    if d3.get() == 1:
        txtNT.config(state=NORMAL)
        VarNT.set("")
    elif d3.get() == 0:
        txtNT.config(state=DISABLED)
        VarNT.set("0")
def RajmaChawal1():
    if d4.get() == 1:
        txtRC.config(state=NORMAL)
        VarRC.set("")
    elif d4.get() == 0:
        txtRC.config(state=DISABLED)
        VarRC.set("0")
def Roti1():
    if d5.get() == 1:
        txtRO.config(state=NORMAL)
        VarRO.set("")
    elif d5.get() == 0:
        txtRO.config(state=DISABLED)
        VarRO.set("0")

def DalMakhni1():
    if d6.get() == 1:
        txtDM.config(state=NORMAL)
        VarDM.set("")
    elif d6.get() == 0:
        txtDM.config(state=DISABLED)
        VarDM.set("0")
def MixVeg1():
    if d7.get() == 1:
        txtMV.config(state=NORMAL)
        VarMV.set("")
    elif d7.get() == 0:
        txtMV.config(state=DISABLED)
        VarMV.set("0")
def Kulcha1():
    if d8.get() == 1:
        txtKU.config(state=NORMAL)
        VarKU.set("")
    elif d8.get() == 0:
        txtKU.config(state=DISABLED)
        VarKU.set("0")
def ShahiPaneer1():
    if d9.get() == 1:
        txtSP.config(state=NORMAL)
        VarSP.set("")
    elif d9.get() == 0:
        txtSP.config(state=DISABLED)
        VarSP.set("0")
#==================================================================================#
def Tea1():
    if e1.get() == 1:
        txtTE.config(state=NORMAL)
        VarTE.set("")
    elif e1.get() == 0:
        txtTE.config(state=DISABLED)
        VarTE.set("0")
def Coffee1():
    if e2.get() == 1:
        txtCF.config(state=NORMAL)
        VarCF.set("")
    elif e2.get() == 0:
        txtCF.config(state=DISABLED)
        VarCF.set("0")
def Cola1():
    if e3.get() == 1:
        txtCO.config(state=NORMAL)
        VarCO.set("")
    elif e3.get() == 0:
        txtCO.config(state=DISABLED)
        VarCO.set("0")
def ChoclateLava1():
    if e4.get() == 1:
        txtCL.config(state=NORMAL)
        VarCL.set("")
    elif e4.get() == 0:
        txtCL.config(state=DISABLED)
        VarCL.set("0")
#==================================================================================#
def IceCream1():
    if e5.get() == 1:
        txtIC.config(state=NORMAL)
        VarIC.set("")
    elif e5.get() == 0:
        txtIC.config(state=DISABLED)
        VarIC.set("0")
def GulabJamun1():
    if e6.get() == 1:
        txtRG.config(state=NORMAL)
        VarGJ.set("")
    elif e6.get() == 0:
        txtRG.config(state=DISABLED)
        VarGJ.set("0")
def Kulfi1():
    if e7.get() == 1:
        txtKUL.config(state=NORMAL)
        VarKUL.set("")
    elif e7.get() == 0:
        txtKUL.config(state=DISABLED)
        VarKUL.set("0")
def Lassi1():
    if e8.get() == 1:
        txtLSSI.config(state=NORMAL)
        VarLSSI.set("")
    elif e8.get() == 0:
        txtLSSI.config(state=DISABLED)
        VarLSSI.set("0")


def FoodorderTotal():
    order1 = int(VarCB.get())*80
    order2 = int(VarNG.get())*90
    order3 = int(VarVG.get())*100
    order4 = int(VarSB.get())*150
    order5 = int(VarVZ.get())*150
    order6 = int(VarNZ.get())*180
    order7 = int(VarCP.get())*120
    order8 = int(VarFP.get())*230
    order9 = int(VarAP.get())*50
    order10 = int(VarGP.get())*60
    order11= int(VarPO.get())*70
    order12= int(VarSW.get())*25
    order13 = int(VarSM.get())*10
    order14 = int(VarBT.get())*20
    order15 = int(VarEO.get())*25
    order16 = int(VarMG.get())*25
    order17 = int(VarPV.get())*70
    order18 = int(VarCBR.get())*110
    order19 = int(VarVT.get())*200
    order20 = int(VarNT.get())*230
    order21 = int(VarRC.get())*90
    order22 = int(VarRO.get())*7
    order23 = int(VarDM.get())*80
    order24 = int(VarMV.get())*70
    order25 = int(VarKU.get())*50
    order26 = int(VarSP.get())*150
    order27 = int(VarTE.get())*10
    order28 = int(VarCF.get())*15
    order29 = int(VarCO.get())*12
    order30 = int(VarCL.get())*70
    order31 = int(VarIC.get())*40
    order32 = int(VarGP.get())*10
    order33 = int(VarKUL.get())*15
    order34=int(VarLSSI.get())*35
    t=round(0.05*(order1+order2+order3 +order4 +order5 +order6 +order7 +order8 +order9+order10+order11+order12+order13 +order14 +order15 +order16+order17 +
                            order18 +order19 +order20 +order21 +order22 +order23 +order24 +order25 +order26 +order27 +order28 +order29 +order30 +order31 +order32+order33 +order34))
    r=(t+order1+order2+order3 +order4 +order5 +order6 +order7 +order8 +order9+order10+order11+order12+order13 +order14 +order15 +order16+order17 +
                            order18 +order19 +order20 +order21 +order22 +order23 +order24 +order25 +order26 +order27 +order28 +order29 +order30 +order31 +order32+order33 +order34)
    Vartotbutton.set(t + order1 + order2 + order3 + order4 + order5 + order6 + order7 + order8 + order9 + order10 + order11 + order12 + order13 + order14 + order15 + order16 + order17 +
                order18 + order19 + order20 + order21 + order22 + order23 + order24 + order25 + order26 + order27 + order28 + order29 + order30 + order31 + order32+order33 +order34)

    t1 = int(EnterAmount1.get())
    VarChangeLabel.set(t1-r)
    if t1-r<0:
        messagebox.showerror("Error", "Insufficient Amount !", parent=root)


# =============================================RESET======================================================================================================#
Reslabel = Button(table5, text="RESET", command=ResetFunction, cursor="hand2", fg="white", bg="purple",font=("times new roman", 15)).place(x=960, y=545, width=180, height=40)




# =============================================Total=========================================================================================#
Varinput=IntVar()
Varinput.set(0)
totbutton = Button(table5, text="TOTAL",cursor="hand2",command=FoodorderTotal, fg="white", bg="purple",font=("times new roman", 15)).place(x=770, y=545, width=180, height=40)
EnterAmount1=Entry(table5, width=20)
EnterAmount1.place(x=800, y=500)
TotalLabel1 = Label(text="Enter Amount (₹)", fg='black', bg="gray64",font=('ariel', 14, 'bold')).place(x=780, y=470)
TotalLabel = Label(text="TOTAL                              ₹", fg='black', bg="gray64",font=('ariel', 14, 'bold')).place(x=1180, y=555)

Vartotbutton = IntVar()
Vartotbutton.set(0)
txt_TotalLabel = tk.Entry(table4, textvariable=Vartotbutton, state=DISABLED, font=("times new roman", 15), width=5).place(x=1420, y=559)

# ------------------------------------------------------------------------------------------------------------------------------------------#
# ============================================CHANGE=======================================================================================#
# ------------------------------------------------------------------------------------------------------------------------------------------#
VarChangeLabel = IntVar()
VarChangeLabel.set(0)
ChangeLabel = Label(text="CHANGE                           ₹", fg='black', bg="gray64",
                    font=('ariel', 14, 'bold')).place(x=1180, y=470)
txt_ChangeLabel = tk.Entry(table4, textvariable=VarChangeLabel, state=DISABLED, font=("times new roman", 15),
                        width=5).place(x=1420, y=470)
# ------------------------------------------------------------------------------------------------------------------------------------------#
# ==========================================------TAX-----=================================================================================#
# ------------------------------------------------------------------------------------------------------------------------------------------#

TaxLabel = Label(text="TAX                                   ₹", fg='black', bg="gray64",
                 font=('ariel', 14, 'bold')).place(x=1180, y=530)
txt_TaxLabel = Label(table4,text='5%', state=DISABLED, font=("times new roman", 15), width=5).place(x=1420,y=530)
# ------------------------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------MENU1------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------------------------------------------#
menu1 = Label(table1, bg='firebrick1', fg='yellow', font=('ariel', 14, 'bold'), text="Burgers").place(x=809, y=109)
a1 = IntVar()
a1.set(0)
VarCB = StringVar()
VarCB.set("0")
Cheese_Burger = Checkbutton(table1,command=Cheesea1, text="CHEESE   ₹80", variable=a1, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=768, y=170)
txtCB = Entry(table1, textvariable=VarCB, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtCB.place(x=915, y=170)
a2 = IntVar()
a2.set(0)
VarNG = StringVar()
VarNG.set("0")
Nonveg_Burger = tk.Checkbutton(table1, text="NON VEG ₹90",command=Nonveg2, variable=a2, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=768, y=200)
txtNG = tk.Entry(table1, textvariable=VarNG, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtNG.place(x=915, y=200)
a3 = IntVar()
a3.set(0)
VarVG = StringVar()
VarVG.set("0")
Veg_Burger = tk.Checkbutton(table1, text="CRISPY VEG ₹100",command=CrispyVeg1, variable=a3, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=768, y=230)
txtVG = tk.Entry(table1, textvariable=VarVG, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtVG.place(x=915, y=230)
a4 = IntVar()
a4.set(0)
VarSB = StringVar()
VarSB.set("0")
special_burger = Checkbutton(table1, text="PIZZA BURGER₹150",command=Pizzaburger1, variable=a4, onvalue=1, offvalue=0,
                             font=('ariel', 8, 'bold')).place(x=768, y=260)
txtSB = tk.Entry(table1, textvariable=VarSB, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtSB.place(x=915, y=260)
# ================================================MENU2=========================================================================================
menu2 = Label(table1, bg='firebrick1', fg='Yellow', font=('ariel', 16, 'bold'), text="Pizza").place(x=809, y=295)
b1 = IntVar()
b1.set(0)
VarVZ = StringVar()
VarVZ.set("0")

Veg_pizza = tk.Checkbutton(table1, text="VEG COMBO ₹150",command=VegPizza1, variable=b1, onvalue=1, offvalue=0,
                        font=('ariel', 8, 'bold')).place(x=768, y=330)
txtVZ =tk.Entry(table1, textvariable=VarVZ, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtVZ.place(x=915, y=330)
b2 = IntVar()
b2.set(0)
VarNZ = StringVar()
VarNZ.set("0")
txtNZ = tk.Entry(table1, textvariable=VarNZ, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtNZ.place(x=915, y=360)
Nonveg_pizza =tk.Checkbutton(table1, text="NONVEG COMBO ₹180",command=NonvegPizza1, variable=b2, onvalue=1, offvalue=0,
                           font=('ariel', 8, 'bold')).place(x=768, y=360)
b3 = IntVar()
b3.set(0)
VarCP = StringVar()
VarCP.set("0")
txtCP = tk.Entry(table1, textvariable=VarCP, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtCP.place(x=915, y=390)
Cheese_pizza = tk.Checkbutton(table1, text="CHEESE  ₹120",command=Cheesepizza1, variable=b3, onvalue=1, offvalue=0,
                           font=('ariel', 8, 'bold')).place(x=768, y=390)
b4 = IntVar()
b4.set(0)
VarFP = StringVar()
VarFP.set("0")
txtFP =tk.Entry(table1, textvariable=VarFP, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtFP.place(x=915, y=420)
Farmhouse_pizza =tk.Checkbutton(table1, text="FARMHOUSE  ₹230",command=Farmhouse1,variable=b4, onvalue=1, offvalue=0,
                              font=('ariel', 8, 'bold')).place(x=768, y=420)

# ------------------------------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------MENU3---------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------------------------------------------#

menu3 = Label(table1, bg='royal blue', fg='Yellow', font=('ariel', 14, 'bold'), text="BreakFast").place(x=1000, y=110)
c1 = IntVar()
c1.set(0)
VarAP = StringVar()
VarAP.set("0")
Aloo_paratha = tk.Checkbutton(table2, text="AlooParatha    ₹50",command=Aloo1, variable=c1, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=970, y=170)
txtAP = tk.Entry(table2, textvariable=VarAP, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtAP.place(x=1115, y=170)
c2 = IntVar()
c2.set(0)
VarGP = StringVar()
VarGP.set("0")
Gobi_paratha = tk.Checkbutton(table1, text="GobiParatha    ₹60",command=Gobi1, variable=c2, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=970, y=200)
txtGP = tk.Entry(table2, textvariable=VarGP, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtGP.place(x=1115, y=200)
c3 = IntVar()
c3.set(0)
VarPO = StringVar()
VarPO.set("0")
Poha = tk.Checkbutton(table2, text="POHA     ₹70", variable=c3,command=Poha1, onvalue=1, offvalue=0, font=('ariel', 8, 'bold')).place(x=970, y=230)
txtPO =tk.Entry(table2, textvariable=VarPO, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtPO.place(x=1115, y=230)
c4 = IntVar()
c4.set(0)
VarSW = StringVar()
VarSW.set("0")
Veg_sandwich = tk.Checkbutton(table2, text="VegSandwich   ₹25", variable=c4,command=VegSandwich1, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=970, y=260)
txtSW = tk.Entry(table2, textvariable=VarSW, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtSW.place(x=1115, y=260)
c5 = IntVar()
c5.set(0)
VarSM = StringVar()
VarSM.set("0")
samosa =tk.Checkbutton(table2, text="Samosa   ₹10",command=Samosa1, variable=c5, onvalue=1, offvalue=0, font=('ariel', 8, 'bold')).place(x=970, y=290)
txtSMSA = tk.Entry(table2, textvariable=VarSW, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtSMSA.place(x=1115, y=290)
c6 = IntVar()
c6.set(0)
VarBT = StringVar()
VarBT.set("0")
Butter_Toast =tk.Checkbutton(table2, text="Butter Toast  ₹20",command=ButterToast1, variable=c6, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=970, y=320)
txtBUTO = tk.Entry(table2, textvariable=VarSW, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtBUTO.place(x=1115, y=320)
c7 = IntVar()
c7.set(0)
VarEO = StringVar()
VarEO.set("0")
Egg_omelet = tk.Checkbutton(table2, text="OMELET     ₹25", variable=c7,command=Omelet1, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=970, y=350)
txtEO =tk.Entry(table2, textvariable=VarSW, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtEO.place(x=1115, y=350)
c8 = IntVar()
c8.set(0)
VarMG = StringVar()
VarMG.set("0")
MAGGI = tk.Checkbutton(table2, text="MASALA MAGGI   ₹25", variable=c8,command=MasalaMaggi1, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=970, y=380)
txtMG = tk.Entry(table2, textvariable=VarMG, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtMG.place(x=1115, y=380)
c9 = IntVar()
c9.set(0)
VarPV = StringVar()
VarPV.set("0")
PAV_BHAJI = tk.Checkbutton(table2, text="PAV BHAJI   ₹70",command=PAVBHAJI1,variable=c9, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=970, y=410)
txtPV =tk.Entry(table2, textvariable=VarPV, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtPV.place(x=1115, y=410)
# ------------------------------------------------------------------------------------------------------------------------------------------#
# -----------------------------------------------------MENU4-------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------------------------------------------#
menu4 = Label(table3, bg='sandy brown', fg='Yellow', font=('ariel', 14, 'bold'), text="Lunch").place(x=1217, y=110)
d1 = IntVar()
d1.set(0)
VarCBR = StringVar()
VarCBR.set("0")
Chole_Bhatura =tk.Checkbutton(table3, text="Chole bhature ₹110", command=Cholebhature1,variable=d1, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=1169, y=170)
txtCBR =tk.Entry(table3, textvariable=VarCBR, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtCBR.place(x=1315, y=170)
d2 = IntVar()
d2.set(0)
VarVT = StringVar()
VarVT.set("0")
VEG_THALI = tk.Checkbutton(table3, text="VEG THALI ₹200", variable=d2,command=VegThali1, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=1169, y=200)
txtVT = tk.Entry(table3, textvariable=VarVT, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtVT.place(x=1315, y=200)
d3 = IntVar()
d3.set(0)
VarNT = StringVar()
VarNT.set("0")
NONVEG_THALI =tk.Checkbutton(table3, text="NONVEG THALI ₹230",command=NonVegThali1, variable=d3, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=1169, y=230)
txtNT =tk.Entry(table3, textvariable=VarNT, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtNT.place(x=1315, y=230)
d4 = IntVar()
d4.set(0)
VarRC = StringVar()
VarRC.set("0")
RAJMA_CHAWAL = tk.Checkbutton(table3, text="RAJMA CHAWAL ₹90",command=RajmaChawal1, variable=d4, onvalue=1, offvalue=0, font=('ariel', 8, 'bold')).place(x=1169, y=260)
txtRC = tk.Entry(table3, textvariable=VarRC, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtRC.place(x=1315, y=260)
d5 = IntVar()
d5.set(0)
VarRO = StringVar()
VarRO.set("0")
ROTI = tk.Checkbutton(table3, text="ROTI ₹7",command=Roti1, variable=d5, onvalue=1, offvalue=0, font=('ariel', 8, 'bold')).place(x=1169,y=290)
txtRO = tk.Entry(table3, textvariable=VarRO, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtRO.place(x=1315, y=290)
d6 = IntVar()
d6.set(0)
VarDM = StringVar()
VarDM.set("0")
DAL_MAKHANI = tk.Checkbutton(table3, text="DAL MAKHANI ₹80",command=DalMakhni1, variable=d6, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=1169, y=320)
txtDM = tk.Entry(table3, textvariable=VarDM, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtDM.place(x=1315, y=320)
d7 = IntVar()
d7.set(0)
VarMV = StringVar()
VarMV.set("0")
MIX_VEG = tk.Checkbutton(table3, text="MIX VEG ₹70",command=MixVeg1, variable=d7, onvalue=1, offvalue=0, font=('ariel', 8, 'bold')).place(x=1169, y=350)
txtMV = tk.Entry(table2, textvariable=VarMV, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtMV.place(x=1315, y=350)
d8 = IntVar()
d8.set(0)
VarKU = StringVar()
VarKU.set("0")
KULCHA = tk.Checkbutton(table3, text="KULCHA ₹50",command=Kulcha1, variable=d8, onvalue=1, offvalue=0, font=('ariel', 8, 'bold')).place(x=1169, y=380)
txtKU = tk.Entry(table3, textvariable=VarKU, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtKU.place(x=1315, y=380)
d9 = IntVar()
d9.set(0)
VarSP = StringVar()
VarSP.set("0")
SHAHI_PANEER = tk.Checkbutton(table1, text="SHAHI PANEER₹150",command=ShahiPaneer1, variable=d9, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=1169, y=410)
txtSP = tk.Entry(table2, textvariable=VarSP, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtSP.place(x=1315, y=410)
# ------------------------------------------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------MENU5-------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------------------------------------------#
menu5 = Label(table4, bg='violetRed1', fg='Yellow', font=('ariel', 14, 'bold'), text="Beverages").place(x=1400, y=110)
e1 = IntVar()
e1.set(0)
VarTE = StringVar()
VarTE.set("0")
TEA = tk.Checkbutton(table4, text="Masala Tea ₹10",command=Tea1, variable=e1, onvalue=1, offvalue=0, font=('ariel', 8, 'bold')).place(
    x=1369, y=170)
txtTE = tk.Entry(table2, textvariable=VarTE, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtTE.place(x=1485, y=170)
e2 = IntVar()
e2.set(0)
VarCF = StringVar()
VarCF.set("0")
COFFEE = tk.Checkbutton(table4, text="COFFEE ₹15",command=Coffee1, variable=e2, onvalue=1, offvalue=0, font=('ariel', 8, 'bold')).place(x=1369, y=200)
txtCF = tk.Entry(table4, textvariable=VarCF, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtCF.place(x=1485, y=200)
e3 = IntVar()
e3.set(0)
VarCO = StringVar()
VarCO.set("0")
COLA = tk.Checkbutton(table4, text="COLA ₹12",command=Cola1, variable=e3, onvalue=1, offvalue=0, font=('ariel', 8, 'bold')).place(x=1369,y=230)
txtCO = tk.Entry(table4, textvariable=VarCO, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtCO.place(x=1485, y=230)
e4 = IntVar()
e4.set(0)
VarCL = StringVar()
VarCL.set("0")
CHOCLATE_LAVA = tk.Checkbutton(table1, text="Choco Lava ₹70",command=ChoclateLava1, variable=e4, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=1369, y=260)
txtCL = tk.Entry(table4, textvariable=VarCL, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtCL.place(x=1485, y=260)
# ------------------------------------------------------------------------------------------------------------------------------------------#
# -------------------------------------------------MENU6-----------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------------------------------------------#
menu6 = Label(table4, bg='violetRed1', fg='Yellow', font=('ariel', 14, 'bold'), text="DESSERT").place(x=1400, y=300)

e5 = IntVar()
e5.set(0)
VarIC = StringVar()
VarIC.set("0")
ICECREAM = tk.Checkbutton(table4, text="Icecream ₹40",command=IceCream1, variable=e5, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=1369, y=330)
txtIC = tk.Entry(table4, textvariable=VarIC, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtIC.place(x=1485, y=330)

e6 = IntVar()
e6.set(0)
VarGJ = StringVar()
VarGJ.set("0")
Gulab_Jamun = tk.Checkbutton(table4, text="GulabJamun ₹10",command=GulabJamun1, variable=e6, onvalue=1, offvalue=0,font=('ariel', 8, 'bold')).place(x=1369, y=360)
txtRG = tk.Entry(table4, textvariable=VarGJ, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtRG.place(x=1485, y=360)

e7 = IntVar()
e7.set(0)
VarKUL = StringVar()
VarKUL.set("0")
KULFI = tk.Checkbutton(table1, text="KULFI ₹15",command=Kulfi1, variable=e7, onvalue=1, offvalue=0, font=('ariel', 8, 'bold')).place(x=1369, y=390)
txtKUL = tk.Entry(table4, textvariable=VarKUL, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtKUL.place(x=1485, y=390)

e8 = IntVar()
e8.set(0)
VarLSSI = StringVar()
VarLSSI.set("0")
LASSI =tk.Checkbutton(table4, text="LASSI ₹35",command=Lassi1, variable=e8, onvalue=1, offvalue=0, font=('ariel', 8, 'bold')).place(x=1369, y=420)
txtLSSI = tk.Entry(table4, textvariable=VarLSSI, width=5, state=DISABLED, font=('ariel', 8, 'bold'))
txtLSSI.place(x=1485, y=420)
def data1():
                  switch=mysql.connector.connect(host="localhost",username="root",password="Fire#100inmyheart",database="foodsys")
                  J=switch.cursor()
                  J.execute("insert into customerdata values(%s,%s,%s,%s,%s,%s)", (order_num_of_cust.get(), name_of_cust.get(),
                                                                         mobile_of_cust.get(), Preference1.get(),
                                                                         Vartotbutton.get(), date2))

                  switch.commit()
                  switch.close()

def place_order1():
             if txt_cname.get() == "" or txt_mobnum.get() == "" or orderlabel1.get()=="":
                    messagebox.showerror("Error", "Empty", parent=root)
             else:
                   messagebox.showinfo("Success","Order has been placed",parent=root)
                   data1()


def exit():
    root.destroy()

place_order = Button(Infoframe, text="Place Order",cursor="hand2",command=place_order1, fg="white", bg="purple",font=("times new roman", 15)).place(x=10, y=454, width=250, height=40)
exit_application = Button(Infoframe, text="Exit",cursor="hand2",command=exit, fg="white", bg="purple",font=("times new roman", 15)).place(x=10, y=524, width=250, height=40)
Bill_b= Button(Infoframe, text="View Bill",cursor="hand2", fg="white", bg="purple",font=("times new roman", 15))
Bill_b.pack(side=BOTTOM)
root.state('zoomed')
root.mainloop()
