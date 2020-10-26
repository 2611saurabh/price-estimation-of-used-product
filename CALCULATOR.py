from tkinter import *


def button():
    print("Thank you for visiting this app :)")


def vechils():
    cost = float(input('enter the cost of vechils::-> '))
    print('confirm vechils module')
    b = float(input('enter km vechiles cover::-> '))
    if b in range(0, 50000):
        print('value', cost / 1.5)
    elif b in range(50001, 100000):
        print('value is', cost / 2)
    elif b in range(100000, 150000):
        print('value', cost / 2.5)
    else:
        print('value', cost / 4)



def Furniture():
    cost = float(input('enter the cost of item'))
    print('Furniture confiremed')
    f = int(input('Enter the month old of furniture'))
    if f in range(0, 3):
        print('value of furniture', cost / 1.5)
    elif f in range(4, 12):
        print('value of furniture', cost / 2)
    else:
        print("SORRY! NOT SOLD")



def Book():
    cost = float(input('enter the cost of item'))
    year = int(input("Enter year of publication::"))
    if year in range(2000, 2010):
        print("Cost of your book is  ", cost / 4)
    elif year in range(2011, 2015):
        print("Cost of your book is  ", cost / 3)
    elif year in range(2016, 2020):
        print("Cost of book is   ", cost / 2)
    else:
        print("BOOK IS TOO OLD WE ARE NOT ABLE TO ESTIMATE THE PRICE  ):")



def Electronics():
    cost = float(input('enter the cost of item'))
    month_used = int(input("how many months old::"))
    if month_used in range(0, 5):
        print("Cost of product is  ", cost / 1.5)
    elif month_used in range(5, 12):
        print("Cost of product is  ", cost / 2)
    else:
        print("Cost of product is  ", cost / 3)



root=Tk()


root.geometry("500x544")


root.minsize(200,200)


root.maxsize(900,900)


welcome=Label(root,text="WELCOME",fg="red",font="Verdana 34 bold",bg="aqua",borderwidth=8)

welcome.grid(row=0,column=3)


n=Label(root,text="Name",font="Verdana 15 bold",fg="blue")
n.grid(row=5,column=1)


p=Label(root,text="Phone",font="Verdana 15 bold",fg="blue")
p.grid(row=7,column=1)


gender=Label(root,text="Gender",font="Verdana 15 bold",fg="blue")
gender.grid(row=9,column=1)


add=Label(root,text="Address",font="Verdana 15 bold",fg="blue")
add.grid(row=11,column=1)


select=Label(root,text="Select the given optin to perform operation",fg="black")
select.grid(row=13,column=2)


nvalue=StringVar()


pvalue=IntVar()


gvalue=StringVar()


addvalue=StringVar()

nameentry=Entry(root,textvariable=nvalue)


phoneentry=Entry(root,textvariable=pvalue)


genderentry=Entry(root,textvariable=gvalue)


addentry=Entry(root,textvariable=addvalue)


nameentry.grid(row=5,column=2)


phoneentry.grid(row=7,column=2)

genderentry.grid(row=9,column=2)


addentry.grid(row=11,column=2)


vechils=Button(root,text="VECHILIS",font="Verdana 12 bold",fg="blue",borderwidth=5,relief=RAISED,command=vechils)
vechils.grid(row=17,column=1)


Furniture=Button(root,text="FURNITURE",font="Verdana 12 bold",fg="blue",borderwidth=5,relief=RAISED,command=Furniture)
Furniture.grid(row=18,column=1)


Book=Button(root,text="BOOK",font="Verdana 12 bold",fg="blue",borderwidth=5,relief=RAISED,command=Book)
Book.grid(row=19,column=1)


Electronics=Button(root,text="Electronics",font="Verdana 12 bold",fg="blue",borderwidth=5,relief=RAISED,command=Electronics)
Electronics.grid(row=20,column=1)


b=Button(root,text="submit",font="Verdana 12 bold",fg="blue",command=button)
b.grid(row=22,column=2)



root.mainloop()