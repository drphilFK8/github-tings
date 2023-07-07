#Tkinter

from tkinter import * 
from tkinter import ttk
import tkinter.messagebox
root= Tk()


root.config(bg= '#FCF6F5')
a = Label(root, text="Grocery List", height= 4, width = 52, bg= "#8A307F", fg= "#6883BC")
a.config(font =("Courier", 20))


label = [Label(root, text="Input grocery:")]
entry = [Entry(root)]
a.pack()
for label, entry in zip(label, entry):
    label.pack()
    entry.pack()

label_quantity = [Label(root, text="Input quantity:")]
entry_quantity = [Entry(root)]
a.pack()
for label_quantity, entry_quantity in zip(label_quantity, entry_quantity):
    label_quantity.pack()
    entry_quantity.pack()


label_price = [Label(root, text="Input price:")]
entry_price = [Entry(root)]
a.pack()
for label_price, entry_price in zip(label_price, entry_price):
    label_price.pack()
    entry_price.pack()

def onClick():
    tkinter.messagebox.showerror("Error")
def offClick():
    tkinter.messagebox.showerror("Use all 3 boxes")

def add_label():
    if entry.get() == "":
        offClick()
    elif entry_quantity.get() == "":
        offClick()
    elif entry_price.get() == "":
        offClick()
    else:

        items_list.append(entry.get())
        quantity_list.append(entry_quantity.get())
        price_list.append(entry_price.get())
        update_list()

def remove_label():
    if txt_output.get('1.0', END+'-1c') ==  "":
       onClick()
    elif txt_quantity.get('1.0', END+'-1c') == "":
        onClick()
    elif txt_price.get('1.0', END+'-1c') == "":
        onClick()
    else:
        txt_output.delete("end-2l","end-1l")
        txt_quantity.delete("end-2l","end-1l")
        txt_price.delete("end-2l","end-1l")
        
        i = 2
        if i ==2 :
            try: items_list.remove(entry.get())
            except: ValueError 

def update_list():
    txt_output.insert(END, items_list[-1] + "\n")
    txt_quantity.insert(END, quantity_list[-1] + "\n")
    txt_price.insert(END, price_list[-1] + "\n")

def calculate():
    txt_calc = Text(root, height=2, width=8, bg= '#79A7D3',fg = 'black')
    txt_calc.pack(pady=(0,0), padx = (0,0) )
    txt_calc.place(x=760, y=300)
    print(calc_list)
    try:
        results = [int(i) for i in calc_list]
        txt_calc.insert(END, sum(results))
    except TypeError:
        onClick()
    







add=ttk.Button(root, text="Add Grocery", command=add_label)
add.pack(anchor=W, pady=10)

remove=ttk.Button(root, text="Remove Grocery", command=remove_label)
remove.pack(anchor=W, pady=10)



txt_output = Text(root, height=30, width=20, bg= '#79A7D3', fg = 'black')


txt_quantity = Text(root, height=30, width=20, bg='#79A7D3', fg = 'black')


txt_price = Text(root, height=30, width=20, bg= '#79A7D3',fg = 'black')


txt_output.pack(pady=(0,0), padx = (0,0))
txt_output.place(x=0, y=390)  

txt_quantity.pack(pady=(25,0), padx = (0,0 ))


txt_price.pack(pady=(0,0), padx = (0,0) )
txt_price.place(x=675, y=390)
txt_output.insert(END, "Items:" + "\n")
txt_price.insert(END, "Price:" + "\n")
txt_quantity.insert(END, "Quantity:" + "\n")


items_list = []

quantity_list = []

price_list = []

calc_list = []
calc_list.append(price_list)


root.mainloop()