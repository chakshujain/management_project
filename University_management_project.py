#======================================Faltu ka kaam=========================================================
from tkinter import *
import random
import datetime
root = Tk()
root.geometry("1600x900+0+0")
root.configure(background = "black")
import tkinter.messagebox

#=========================================Frames=============================================================

Top = Frame(root,width = 1600, height = 100, border = 16, relief = "raise")
Top.pack(side = TOP)
f5= Frame(root,width = 1600,height = 200,border = 12, relief = "raise")
f5.pack(side= BOTTOM)




f1 = Frame(root,width = 350,height = 600,border = 16, relief = "raise")
f1.pack(side= LEFT)
f2 = Frame(root,width = 350,height = 600,border = 16, relief = "raise")
f2.pack(side= LEFT)
f3 = Frame(root,width = 350,height = 600,border = 16, relief = "raise")
f3.pack(side= LEFT)
f4 = Frame(root,width = 550,height = 600,border = 16, relief = "raise")
f4.pack(side= LEFT)

#=======================================================Database==================================================================
database = [(11172591,1000),(11172597,1000),(11172542,1000)]
    



#==================================CHECKBOXES SET AS ZERO==================================
uniform_pairvar = IntVar()


bedsheetvar = IntVar()


blanketvar = IntVar()


towelvar = IntVar()


drycleanvar = IntVar()


suitvar = IntVar()


denimsvar = IntVar()


shirtvar = IntVar()


breakfastvar = IntVar()


lunchvar = IntVar()


dinnervar = IntVar()


drinksvar = IntVar()


noodlesvar = IntVar()



shakevar = IntVar()

burgervar = IntVar()


icecreamvar = IntVar()



notebooksvar = IntVar()



photocopycolorvar = IntVar()


photocopybwvar = IntVar()



printsvar = IntVar()



practicalsvar = IntVar()



normalfilesvar = IntVar()
normalfilesvar.set(0)


diariesvar = IntVar()



pensvar = IntVar()

#===============================================Textvariables for entries===============================================

Euniform_pair = StringVar()
Ebedsheet = StringVar()
Eblanket = StringVar()
Etowel = StringVar()
Edryclean = StringVar()
Esuit = StringVar()
Edenims = StringVar()
Eshirt = StringVar()
Ebreakfast = StringVar()
Elunch= StringVar()
Edinner = StringVar()
Edrinks = StringVar()
Enoodles = StringVar()
Eshake = StringVar()
Eburger = StringVar()
Eicecream = StringVar()
Enotebooks = StringVar()
Ephotocopycolor = StringVar()
Ephotocopybw = StringVar()
Eprints = StringVar()
Epracticals = StringVar()
Enormalfiles = StringVar()
Ediaries = StringVar()
Epens = StringVar()



Euniform_pair.set("0")
Ebedsheet.set("0")
Eblanket.set("0")
Etowel.set("0")
Edryclean.set("0")
Esuit.set("0")
Edenims.set("0")
Eshirt.set("0")
Ebreakfast.set("0")
Elunch.set("0")
Edinner.set("0")
Edrinks.set("0")
Enoodles.set("0")
Eshake.set("0")
Eburger.set("0")
Eicecream.set("0")
Enotebooks.set("0")
Ephotocopycolor.set("0")
Ephotocopybw.set("0")
Eprints.set("0")
Epracticals.set("0")
Enormalfiles.set("0")
Ediaries.set("0")
Epens.set("0")



#===============================================FUNCTIONS===============================================================
    
        

def reset():

    receipt_txt.delete('1.0', END)
    
    uniform_pairvar.set(0)
    bedsheetvar.set(0)    
    blanketvar.set(0)
    towelvar.set(0)
    drycleanvar.set(0)
    suitvar.set(0)
    denimsvar.set(0)
    shirtvar.set(0)
    breakfastvar.set(0)
    lunchvar.set(0)
    dinnervar.set(0)
    drinksvar.set(0)
    noodlesvar.set(0)
    shakevar.set(0)
    burgervar.set(0)
    icecreamvar.set(0)
    notebooksvar.set(0)
    photocopycolorvar.set(0)
    photocopybwvar.set(0)
    printsvar.set(0)
    practicalsvar.set(0)
    normalfilesvar.set(0)
    diariesvar.set(0)
    pensvar.set(0)        


    Euniform_pair.set("0")
    Ebedsheet.set("0")
    Eblanket.set("0")
    Etowel.set("0")
    Edryclean.set("0")
    Esuit.set("0")
    Edenims.set("0")
    Eshirt.set("0")
    Ebreakfast.set("0")
    Elunch.set("0")
    Edinner.set("0")
    Edrinks.set("0")
    Enoodles.set("0")
    Eshake.set("0")
    Eburger.set("0")
    Eicecream.set("0")
    Enotebooks.set("0")
    Ephotocopycolor.set("0")
    Ephotocopybw.set("0")
    Eprints.set("0")
    Epracticals.set("0")
    Enormalfiles.set("0")
    Ediaries.set("0")
    Epens.set("0")
    Eamt_payable.set("0")

    uniform_paire.configure(state = DISABLED)
    bedsheete.configure(state = DISABLED)
    blankete.configure(state = DISABLED)
    towele.configure(state = DISABLED)
    drycleane.configure(state = DISABLED)
    suite.configure(state = DISABLED)
    denimse.configure(state = DISABLED)
    shirte.configure(state = DISABLED)
    breakfaste.configure(state = DISABLED)
    lunche.configure(state = DISABLED)
    dinnere.configure(state = DISABLED)
    drinkse.configure(state = DISABLED)
    noodlese.configure(state = DISABLED)
    shakee.configure(state = DISABLED)
    burgere.configure(state = DISABLED)
    icecreame.configure(state = DISABLED)
    notebookse.configure(state = DISABLED)
    photocopycolore.configure(state = DISABLED)
    photocopybwe.configure(state = DISABLED)
    printse.configure(state = DISABLED)
    practicalse.configure(state = DISABLED)
    normalfilese.configure(state = DISABLED)
    diariese.configure(state = DISABLED)
    pense.configure(state = DISABLED)
    


def chkbutton_value():
    if(uniform_pairvar.get()==1):
        uniform_paire.configure(state = NORMAL)
    elif(uniform_pairvar.get()==0):
        uniform_paire.configure(state = DISABLED)
        Euniform_pair.set("0")
    if(bedsheetvar.get()==1):
        bedsheete.configure(state = NORMAL)
    elif(bedsheetvar.get()==0):
        bedsheete.configure(state = DISABLED)
        Ebedsheet.set("0")
    if(blanketvar.get()==1):
        blankete.configure(state = NORMAL)
    elif(blanketvar.get()==0):
        blankete.configure(state = DISABLED)
        Eblanket.set("0")
    if(towelvar.get()==1):
        towele.configure(state = NORMAL)
    elif(towelvar.get()==0):
        towele.configure(state = DISABLED)
        Etowel.set("0")
    if(drycleanvar.get()==1):
        drycleane.configure(state = NORMAL)
    elif(drycleanvar.get()==0):
        drycleane.configure(state = DISABLED)
        Edryclean.set("0")
    if(suitvar.get()==1):
        suite.configure(state =  NORMAL)
    elif(suitvar.get()==0):
        suite.configure(state = DISABLED)
        Esuit.set("0")
    if(denimsvar.get()==1):
        denimse.configure(state =  NORMAL)
    elif(denimsvar.get()==0):
        denimse.configure(state = DISABLED)
        Edenims.set("0")
    if(shirtvar.get()==1):
        shirte.configure(state =  NORMAL)
    elif(shirtvar.get()==0):
        shirte.configure(state = DISABLED)
        Eshirt.set("0")
    if(breakfastvar.get()==1):
        breakfaste.configure(state =  NORMAL)
    elif(breakfastvar.get()==0):
        breakfaste.configure(state = DISABLED)
        Ebreakfast.set("0")
    if(lunchvar.get()==1):
        lunche.configure(state = NORMAL)
    elif(lunchvar.get==0):
        lunche.configure(state = DISABLED)
        Elunch.set("0")
    if(dinnervar.get()==1):
        dinnere.configure(state =  NORMAL)
    elif(dinnervar.get()==0):
        dinnere.configure(state = DISABLED)
        Edinner.set("0")
    if(drinksvar.get()==1):
        drinkse.configure(state =  NORMAL)
    elif(drinksvar.get()==0):
        drinkse.configure(state = DISABLED)
        Edrinks.set("0")
    if(noodlesvar.get()==1):
        noodlese.configure(state =  NORMAL)
    elif(noodlesvar.get()==0):
        noodlese.configure(state = DISABLED)
        Enoodles.set("0")
    if(shakevar.get()==1):
        shakee.configure(state =  NORMAL)
    elif(shakevar.get()==0):
        shakee.configure(state = DISABLED)
        Eshake.set("0")
    if(burgervar.get()==1):
        burgere.configure(state = NORMAL)
    elif(burgervar.get()==0):
        burgere.configure(state = DISABLED)
        Eburger.set("0")
    if(icecreamvar.get()==1):
        icecreame.configure(state =  NORMAL)
    elif(icecreamvar.get()==0):
        icecreame.configure(state = DISABLED)
        Eicecream.set("0")
    if(notebooksvar.get()==1):
        notebookse.configure(state =  NORMAL)
    elif(notebooksvar.get()==0):
        notebookse.configure(state = DISABLED)
        Enotebooks.set("0")
    if(photocopycolorvar.get()==1):
        photocopycolore.configure(state =  NORMAL)
    elif(photocopycolorvar.get()==0):
        photocopycolore.configure(state = DISABLED)
        Ephotocopycolor.set("0")
    if(photocopybwvar.get()==1):
        photocopybwe.configure(state =  NORMAL)
    elif(photocopybwvar.get()==0):
        photocopybwe.configure(state = DISABLED)
        Ephotocopybw.set("0")
    if(printsvar.get() == 1):
        printse.configure(state =  NORMAL)
    elif(printsvar.get()==0):
        printse.configure(state = DISABLED)
        Eprints.set("0")
    if(practicalsvar.get()==1):
        practicalse.configure(state =  NORMAL)
    elif(practicalsvar.get()==0):
        practicalse.configure(state = DISABLED)
        Epracticals.set("0")
    if(normalfilesvar.get()==1):
        normalfilese.configure(state =  NORMAL)
    elif(normalfilesvar.get()==0):
        normalfilese.configure(state = DISABLED)
        Enormalfiles.set("0")
    if(diariesvar.get()==1):
        diariese.configure(state =  NORMAL)
    elif(diariesvar.get()==0):
        diariese.configure(state = DISABLED)
        Ediaries.set("0")
    if(pensvar.get()==1):
        pense.configure(state = NORMAL)
    elif(pensvar.get()==0):
        pense.configure(state = DISABLED)
        Epens.set("0")


#==================================================================Total cost================================================
        
        

    
def total():
    Eamt_payable.set(str(int(Euniform_pair.get())*10 + int(Ebedsheet.get())*20 + int(Eblanket.get())*10 + int(Etowel.get())*5 + int(Edryclean.get())*500 + int(Esuit.get())*100 + int(Edenims.get())*15 +int(Eshirt.get())*5 + int(Ebreakfast.get())*30 + int(Elunch.get())*50 + int(Edinner.get())*60 + int(Edrinks.get())*35 +int(Enoodles.get())*40 + int(Eshake.get())*30 + int(Eburger.get())*25 + int(Eicecream.get())*25 + int(Enotebooks.get())*20 + int(Ephotocopycolor.get())*5 + int(Ephotocopybw.get())*2 + int(Eprints.get())*10 + int(Epracticals.get())*110 + int(Enormalfiles.get())*15 + int(Ediaries.get())*90 + int(Epens.get())*5))


def quite():
    quite = tkinter.messagebox.askyesno("Quit","DO you really wanna quit?")
    if quite>0:
        root.destroy()
    else:
        return


#===============================================================RECIPT============================================================    



def print_recipt():
    receipt_txt.insert(END,f"Bill No. {random.randint(10000,999999)} \n")
    receipt_txt.insert(END,f"{datetime.datetime.now()} \n")
    receipt_txt.insert(END,"Uniform Pair \t "  + Euniform_pair.get() + " *10 \t" + "=  " + str(int(Euniform_pair.get())*10) + "\n" )
    receipt_txt.insert(END,"Bedsheet \t "  + Ebedsheet.get() + " *20 \t" + "=  " + str(int(Ebedsheet.get())*20)+ "\n"  )
    receipt_txt.insert(END,"Blanket \t "  + Eblanket.get() + " *10 \t" + "=  " + str(int(Eblanket.get())*10)+ "\n"  )
    receipt_txt.insert(END,"Towel \t "  + Etowel.get() + " *5 \t" + "=  " + str(int(Etowel.get())*5)+ "\n"  )
    receipt_txt.insert(END,"Dryclean\t "  + Edryclean.get() + " *500 \t" + "=  " + str(int(Edryclean.get())*500) + "\n" )
    receipt_txt.insert(END,"Suit \t "  + Esuit.get() + " *100 \t" + "=  " + str(int(Esuit.get())*100)+ "\n"  )
    receipt_txt.insert(END,"Denims \t "  + Edenims.get() + " *15 \t" + "=  " + str(int(Edenims.get())*15) + "\n" )
    receipt_txt.insert(END,"shirt \t "  + Eshirt.get() + " *5 \t" + "=  " + str(int(Eshirt.get())*5)+ "\n"  )
    receipt_txt.insert(END,"Breakfast \t "  + Ebreakfast.get() + " *30 \t" + "=  " + str(int(Ebreakfast.get())*30)+ "\n"  )
    receipt_txt.insert(END,"Lunch \t "  + Elunch.get() + " *50 \t" + "=  " + str(int(Elunch.get())*50) + "\n" )
    receipt_txt.insert(END,"Dinner\t "  + Edinner.get() + " *60 \t" + "=  " + str(int(Edinner.get())*60) + "\n" )
    receipt_txt.insert(END,"Drinks \t "  + Edrinks.get() + " *35 \t" + "=  " + str(int(Edrinks.get())*35)+ "\n"  )
    receipt_txt.insert(END,"Noodles \t "  + Enoodles.get() + " *40 \t" + "=  " + str(int(Enoodles.get())*40)+ "\n"  )
    receipt_txt.insert(END,"Shake\t "  + Eshake.get() + " *30 \t" + "=  " + str(int(Eshake.get())*30)+ "\n"  )
    receipt_txt.insert(END,"Burger \t "  + Eburger.get() + " *25 \t" + "=  " + str(int(Eburger.get())*25)+ "\n"  )
    receipt_txt.insert(END,"Icecream \t "  + Eicecream.get() + " *25 \t" + "=  " + str(int(Eicecream.get())*25) + "\n" )
    receipt_txt.insert(END,"Notebooks\t "  + Enotebooks.get() + " *20 \t" + "=  " + str(int(Enotebooks.get())*20) + "\n" )
    receipt_txt.insert(END,"Coloured Photocopy \t "  + Ephotocopycolor.get() + " *5 \t" + "=  " + str(int(Ephotocopycolor.get())*5)+ "\n"  )
    receipt_txt.insert(END,r"B/W Photocopy \t "  + Ephotocopybw.get() + " *2 \t" + "=  " + str(int(Ephotocopybw.get())*2)+ "\n"  )
    receipt_txt.insert(END,"Prints \t "  + Eprints.get() + " *10 \t" + "=  " + str(int(Eprints.get())*10)+ "\n"  )
    receipt_txt.insert(END,"Practicals \t "  + Epracticals.get() + " *110 \t" + "=  " + str(int(Epracticals.get())*110)+ "\n"  )
    receipt_txt.insert(END,"Normal Files\t "  + Enormalfiles.get() + " *15 \t" + "=  " + str(int(Enormalfiles.get())*15) + "\n" )
    receipt_txt.insert(END,"Diaries \t "  + Ediaries.get() + " *100 \t" + "=  " + str(int(Ediaries.get())*100)+ "\n"  )
    receipt_txt.insert(END,"Pens \t "  + Epens.get() + " *5 \t" + "=  " + str(int(Epens.get())*5) )
    receipt_txt.insert(END,"Amount Paid \t "  +" = "+ Eamt_payable.get() )
       
roll_numvar = StringVar()
labelvar= StringVar()
    
operator = ""    
    
def mail():
    pass

    
def payment():
    pay = Toplevel()
    pay.geometry("300x200+0+0") 
    label = Label(pay,text = "Enter roll no or scan barcode", font = ("arial",15,"bold"),bd = 5).grid(row = 0,column = 0)
    roll_num = Entry(pay,textvariable = roll_numvar,font = ("arial",15,"bold"),bd = 5)
    roll_num.grid(row = 1,column = 0)
    paybtn = Button(pay,text = "PAY",font = ("arial",15,"bold"),bd = 5,command = abc).grid(row= 2,column = 0)
    label = Label(pay,textvariable = labelvar, font = ("arial",10,"bold"),bd = 5,width = 30).grid(row = 3,column = 0)
def abc():
    labelvar.set("Payment Successful")
        
  
   
    
    

      
         
     
#=============================================================================Calculator===============================================================================

def calculator():
    
    cal = Toplevel(root)
    cal.geometry("350x480+0+0")
    text_input = StringVar()
    

    def btnClick(numbers):
        global operator
        operator = operator +str(numbers)
        text_input.set(operator)
    def btnclear():
        global operator
        operator = ""
        text_input.set("")
    def btnequals():
        global operator
        sumup = str(eval(operator))
        text_input.set(sumup)
        operator = ""

    txtDisplay = Entry(cal,font = ("arial",20,"bold"),textvariable=text_input,bd = 30,bg = "powder blue",justify = "right")
    txtDisplay.grid(columnspan = 4)

    btn7 = Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "7",bg = "powder blue",command= lambda : btnClick(7) )
    btn7.grid(row = 1,column = 0)


    btn8 = Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "8",bg = "powder blue",command= lambda : btnClick(8) )
    btn8.grid(row = 1,column = 1)


    btn9= Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "9",bg = "powder blue",command= lambda : btnClick(9) )
    btn9.grid(row = 1,column = 2)


    btn4 = Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "4",bg = "powder blue",command= lambda : btnClick(4) )
    btn4.grid(row = 2,column = 0)


    btn5 = Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "5",bg = "powder blue",command= lambda : btnClick(5) )
    btn5.grid(row = 2,column = 1)


    btn6 = Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "6",bg = "powder blue",command= lambda : btnClick(6) )
    btn6.grid(row = 2,column = 2)


    btn1= Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "1",bg = "powder blue",command= lambda : btnClick(1) )
    btn1.grid(row = 3,column = 0)


    btn2 = Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "2",bg = "powder blue",command= lambda : btnClick(2) )
    btn2.grid(row = 3,column = 1)


    btn3 = Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "3",bg = "powder blue",command= lambda : btnClick(3) )
    btn3.grid(row = 3,column = 2)

    addition= Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "+",bg = "powder blue",command= lambda : btnClick("+") )
    addition.grid(row = 1,column = 3)


    substraction = Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "-",bg = "powder blue",command= lambda : btnClick("-") )
    substraction.grid(row = 2,column = 3)

    multiply = Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "*",bg = "powder blue",command= lambda : btnClick("*") )
    multiply.grid(row = 3,column = 3)


    divison = Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "/",bg = "powder blue",command= lambda : btnClick("/") )
    divison.grid(row = 4,column = 3)



    btn0 = Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "0",bg = "powder blue",command= lambda : btnClick(0) )
    btn0.grid(row = 4,column = 0)

    btnequals = Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "=",bg = "powder blue",command=btnequals )
    btnequals.grid(row = 4,column = 2)


    btnclear = Button(cal,padx = 16,pady = 16,bd = 8,fg = "black",font = ("arial",20,"bold"),text= "C",bg = "powder blue",command=  btnclear )
    btnclear.grid(row = 4,column = 1)


        



    
    

    
    
    





#===============================================LABELS AND CHECKBUTTONS==============================================================

label_info = Label(Top,text = "MAHARISHI MARKENDESHAR UNIVERSITY, MULLANA , AMBALA",font = ("arial",35,"bold"),border = 16,fg = "red")
label_info.grid(row = 0, column = 0)

laundary_label = Label(f1,text = "LAUNDRY",font = ("arial",20,"bold"),border = 7,fg = "red")
laundary_label.grid(row = 0,column = 0)

uniform_pair = Checkbutton(f1,text = "Uniform",variable = uniform_pairvar, font = ("arial",20,"bold"),border = 5,onvalue = 1,offvalue = 0,command = chkbutton_value,fg = "blue")
uniform_pair.grid(row = 1,sticky = W)

bedsheet = Checkbutton(f1,variable =bedsheetvar, text = "Bedsheet",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue" )
bedsheet.grid(row = 2,sticky = W)

blanket = Checkbutton(f1,variable =blanketvar, text = "Blanket",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
blanket.grid(row = 3,sticky = W)

towel = Checkbutton(f1,variable =towelvar, text = "Towel",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
towel.grid(row = 4,sticky = W)

dryclean = Checkbutton(f1,variable =drycleanvar, text = "DryClean",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
dryclean.grid(row = 5,sticky = W)

suit = Checkbutton(f1,variable =suitvar, text = "Suit",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
suit.grid(row = 6,sticky = W)

denims = Checkbutton(f1,variable =denimsvar, text = "Denims",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
denims.grid(row = 7,sticky = W)

shirt = Checkbutton(f1,variable =shirtvar, text = "Shirt",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
shirt.grid(row = 8,sticky = W)




fooding_label = Label(f2,text = "FOODING",font = ("arial",20,"bold"),border = 7,fg = "red")
fooding_label.grid(row = 0,column = 0)

breakfast = Checkbutton(f2,variable =breakfastvar, text = "Breakfast",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
breakfast.grid(row = 1,sticky = W)

lunch = Checkbutton(f2,variable =lunchvar, text = "Lunch",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
lunch.grid(row = 2,sticky = W)

dinner = Checkbutton(f2,variable =dinnervar, text = "Dinner",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
dinner.grid(row =3 ,sticky = W)



drinks = Checkbutton(f2,variable =drinksvar, text = "Drinks",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
drinks.grid(row = 4,sticky = W)

noodles = Checkbutton(f2,variable =noodlesvar, text = "Noodles",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
noodles.grid(row = 5,sticky = W)

shake = Checkbutton(f2,variable =shakevar, text = "Shakes",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
shake.grid(row = 6,sticky = W)

burger = Checkbutton(f2,variable =burgervar, text = "Burgers",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
burger.grid(row = 7,sticky = W)

icecream= Checkbutton(f2,variable =icecreamvar, text = "Ice Cream",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
icecream.grid(row = 8,sticky = W)




stationary_label = Label(f3,text = "STATIONARY",font = ("arial",20,"bold"),border = 7,fg = "red")
stationary_label.grid(row = 0,column = 0)

notebooks = Checkbutton(f3,variable =notebooksvar, text = "Notebooks",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
notebooks.grid(row = 1,sticky = W)

photocopycolor = Checkbutton(f3,variable =photocopycolorvar, text = r"Photocopy(color)",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
photocopycolor.grid(row = 2,sticky = W)

photocopybw = Checkbutton(f3,variable =photocopybwvar, text = r"Photocopy(b/w)",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
photocopybw.grid(row = 3,sticky = W)

prints = Checkbutton(f3,variable =printsvar, text = "Prints",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
prints.grid(row = 4,sticky = W)

practicals = Checkbutton(f3,variable =practicalsvar, text = "Practicals",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
practicals.grid(row = 5,sticky = W)

normalfiles= Checkbutton(f3,variable =normalfilesvar, text = "Normal files",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
normalfiles.grid(row = 6,sticky = W)

diaries= Checkbutton(f3,variable =diariesvar, text = "Diaries",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
diaries.grid(row = 7,sticky = W)

pens = Checkbutton(f3,variable =pensvar, text = "Pens",font = ("arial",20,"bold"),border = 5,command = chkbutton_value,fg = "blue")
pens.grid(row = 8,sticky = W)

#=====================================================ENTRIES==================================================================


uniform_paire = Entry(f1,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Euniform_pair,bg = "powder blue")
uniform_paire.grid(row = 1,column = 1)


bedsheete = Entry(f1,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable =Ebedsheet,bg = "powder blue")
bedsheete.grid(row = 2,column = 1)


blankete = Entry(f1,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable =Eblanket,bg = "powder blue")
blankete.grid(row = 3,column = 1)


towele = Entry(f1,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Etowel,bg = "powder blue")
towele.grid(row = 4,column = 1)


drycleane = Entry(f1,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Edryclean,bg = "powder blue")
drycleane.grid(row = 5,column = 1)


suite = Entry(f1,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Esuit,bg = "powder blue")
suite.grid(row = 6,column = 1)


denimse = Entry(f1,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Edenims,bg = "powder blue")
denimse.grid(row = 7,column = 1)


shirte = Entry(f1,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable =Eshirt,bg = "powder blue")
shirte.grid(row = 8,column = 1)


breakfaste = Entry(f2,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Ebreakfast,bg = "powder blue")
breakfaste.grid(row = 1,column = 1)

lunche = Entry(f2,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Elunch,bg = "powder blue")
lunche.grid(row = 2,column = 1)

dinnere = Entry(f2,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Edinner,bg = "powder blue")
dinnere.grid(row = 3,column = 1)

drinkse = Entry(f2,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Edrinks,bg = "powder blue")
drinkse.grid(row = 4,column = 1)


noodlese = Entry(f2,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Enoodles,bg = "powder blue")
noodlese.grid(row = 5,column = 1)


shakee = Entry(f2,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Eshake,bg = "powder blue")
shakee.grid(row = 6,column = 1)

burgere = Entry(f2,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable =Eburger,bg = "powder blue")
burgere.grid(row = 7,column = 1)

icecreame = Entry(f2,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Eicecream,bg = "powder blue")
icecreame.grid(row = 8,column = 1)

notebookse = Entry(f3,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Enotebooks,bg = "powder blue")
notebookse.grid(row = 1,column = 1)

photocopycolore = Entry(f3,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Ephotocopycolor,bg = "powder blue")
photocopycolore.grid(row = 2,column = 1)

photocopybwe = Entry(f3,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable =Ephotocopybw,bg = "powder blue")
photocopybwe.grid(row = 3,column = 1)

printse = Entry(f3,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Eprints,bg = "powder blue")
printse.grid(row = 4,column = 1)


practicalse = Entry(f3,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Epracticals,bg = "powder blue")
practicalse.grid(row = 5,column = 1)


normalfilese = Entry(f3,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Enormalfiles,bg = "powder blue")
normalfilese.grid(row = 6,column = 1)

diariese = Entry(f3,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Ediaries,bg = "powder blue")
diariese.grid(row = 7,column = 1)

pense = Entry(f3,font = ("arial",20,"bold"),border = 4, width = 6,justify = "left",state = DISABLED,textvariable = Epens,bg = "powder blue")
pense.grid(row = 8,column = 1)

#===============================================RECEIPT===================================================================


receipt_label = Label(f4,text = "Receipt",font = ("arial",20,"bold"),border = 2,anchor = "w")
receipt_label.grid(row = 0,column = 0)



receipt_txt = Text(f4,font = ("arial",20,"bold"),bg = "white",bd = 5,width = 32,height = 13)
receipt_txt.grid(row = 1,column = 0)



#==================================================BUTTONS====================================================================




btnTotal = Button(f5,padx = 10,pady = 1,text = "TOTAL",font = ("arial",20,"bold"),fg = "black",bd = 5,command = total).grid(row = 0,column = 2)

btnReset = Button(f5,padx = 10,pady = 1,text = "RESET",font = ("arial",20,"bold"),fg = "black",bd = 5,command = reset).grid(row = 0,column = 3)

btnquit = Button(f5,padx = 10,pady = 1,text = "QUIT",font = ("arial",20,"bold"),fg = "black",bd = 5,command = quite).grid(row = 0,column = 4)

btnrecipt = Button(f5,padx = 10,pady = 1,text = "Print Recipt",font = ("arial",20,"bold"),fg = "black",bd = 5,command = print_recipt).grid(row = 0,column = 5)

btnmail = Button(f5,padx = 10,pady = 1,text = "Send Mail",font = ("arial",20,"bold"),fg = "black",bd = 5,command = mail).grid(row = 1,column = 1)

btnpaybycash = Button(f5,padx = 10,pady = 1,text = "Pay By Cash",font = ("arial",20,"bold"),fg = "black",bd = 5,command = print_recipt).grid(row = 1)

btnpaybycard = Button(f5,padx = 10,pady = 1,text = "Pay By ID Card",font = ("arial",20,"bold"),fg = "black",bd = 5,command = payment).grid(row = 0,column = 7)



Eamt_payable = StringVar()


labelamt = Label(f5,text = "Amount Payable",font = ("arial",20,"bold"),bd = 6).grid(row = 0,column = 0)
amt_payable = Entry(f5,width =8,font = ("arial",20,"bold"),bd = 6,textvariable = Eamt_payable)
amt_payable.grid(row = 0,column = 1)

btnCalc = Button(f5,padx = 10,pady = 1,text = "Calculator",font = ("arial",20,"bold"),fg = "black",bd = 5,command = calculator).grid(row = 0,column = 6)












root.mainloop()
