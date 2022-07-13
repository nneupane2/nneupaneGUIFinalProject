from tkinter import *

win = Tk()
var = IntVar()
win.title("Peter's Pizza Palace")
win.geometry("640x480")
win.configure(bg="blue")

label = Label(win, text="Peter's Pizza Palace", font=("Arial", 35), bg="grey", fg="black")
label.grid(row=0, column=0, columnspan=4, padx=30, pady=20)

label10 = Label(win, text="Choose your Size", font=("Arial", 20), bg="black", fg="White")
label10.grid(row=1, column=0, ipadx=20, ipady=10, padx=10, pady=10)

label2 = Label(win, text="Choose your Crust", font=("Arial", 20), bg="black", fg="White")
label2.grid(sticky="w", row=6, column=0, ipadx=20, ipady=10, padx=10)

label3 = Label(win, text="Choose your Flavour", font=("Arial", 20), bg="black", fg="White")
label3.grid(sticky="w", row=1, column=3, ipadx=20, ipady=10, padx=10, pady=10)

label2 = Label(win, text="Choose your Topping", font=("Arial", 20), bg="black", fg="white")
label2.grid(row=1, column=4, ipadx=20, ipady=10, padx=10, pady=10)

label3 = Label(win, text="Choose your Sauce", font=("Arial", 20), bg="black", fg="white")
label3.grid(row=1, column=5, ipadx=20, ipady=10, padx=10, pady=10, sticky="w")

label4 = Label(win, text="Choose your Drink", font=("Minion Pro Cond", 20), bg="black", fg="white")
label4.grid(row=6, column=5, ipadx=20, ipady=10, padx=10, pady=10, sticky="w")

u_list = []
## you can also do grid inside pack frame unlike other scenarios

r = IntVar()
r.set(2)
flavours = ["Sicilian Tikka", "Morrocon Fajita", "Buffalo Ranch", "Margherita", "Habenero", "All Cheese", "All Veggie",
            "Supereme Max"]
flavour = StringVar()
flavour.set("Sicilian Tikka")


def nextt():
    global u_list
    u_list = u_list[-1:]
    print(u_list)


def click(value):
    u_list.append(value)


for i in range(len(flavours)):
    Radiobutton(win, text=flavours[i], variable=flavour, width=12, height=3, bg="green", value=flavours[i],
                activebackground="red", anchor=W, command=lambda: click(flavour.get())).grid(row=i + 2, column=3,
                                                                                             padx=10, pady=10,
                                                                                             sticky="w")

v_list = []
## you can also do grid inside pack frame unlike other scenarios

r = IntVar()
r.set(2)
sizes = ["Small", "Medium", "Large"]
size = StringVar()
size.set("Small")


def nextt():
    global v_list
    v_list = v_list[-1:]
    print(v_list)


def click(value):
    v_list.append(value)


for i in range(len(sizes)):
    Radiobutton(win, text=sizes[i], variable=size, width=10, height=3, bg="green", value=sizes[i],
                activebackground="red", anchor=W, command=lambda: click(size.get())).grid(row=i + 2, column=0, padx=10,
                                                                                          pady=10, sticky="w")

m_list = []
## you can also do grid inside pack frame unlike other scenarios

r = IntVar()
r.set(2)
toppings = ["Olives", "Halepenos", "Red Pepper", "Pepperoni", "Mushrooms", "Tomatoes", "Chilli", "Capsicum"]
topping = StringVar()
topping.set("Olives")


def nextt():
    global m_list
    m_list = m_list[-1:]
    print(m_list)


def click(value):
    m_list.append(value)


for i in range(len(toppings)):
    Radiobutton(win, text=toppings[i], variable=topping, width=12, height=3, bg="green", value=toppings[i],
                activebackground="red", anchor=W, command=lambda: click(topping.get())).grid(row=i + 2, column=4,
                                                                                             padx=10, pady=10,
                                                                                             sticky="w")

d_list = []
## you can also do grid inside pack frame unlike other scenarios

r = IntVar()
r.set(2)
sauces = ["Mayo Garlic", "Barbecue", "Buffalo Ranch"]
sauce = StringVar()
sauce.set("Mayo Garlic")


def nextt():
    global d_list
    d_list = d_list[-1:]
    print(d_list)


def click(value):
    d_list.append(value)


for i in range(len(sauces)):
    Radiobutton(win, text=sauces[i], variable=sauce, width=12, height=3, bg="green", value=sauces[i],
                activebackground="red", anchor=W, command=lambda: click(sauce.get())).grid(row=i + 2, column=5, padx=10,
                                                                                           pady=10, sticky="w")

a_list = []
## you can also do grid inside pack frame unlike other scenarios

r = IntVar()
r.set(2)
drinks = ["Pepsi", "Fanta", "Sprite", "Water", "Coke", "Coca-Cola", "Mountain Dew", "Dr Pepper", "Diet Coke", "Diet Pepsi"]
drink = StringVar()
drink.set("Pepsi")


def nextt():
    global a_list
    a_list = a_list[-1:]
    print(a_list)


def click(value):
    a_list.append(value)


for i in range(len(drinks)):
    Radiobutton(win, text=drinks[i], variable=drink, width=12, height=3, bg="green", value=drinks[i],
                activebackground="red", anchor=W, command=lambda: click(drink.get())).grid(row=i + 7, column=5, padx=10,
                                                                                           pady=10, sticky="w")

win.mainloop()