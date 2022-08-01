from tkinter import *
from tkinter import messagebox
import Calculator as cl
 
def clear():
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
 
 
def display():
    a = name_entry.get()
    b = surname_entry.get()
    messagebox.showinfo("GUI Python", cl.main(a, b))

root = Tk()
root.title("GUI на Python")

root.geometry("400x300")

name_label = Label(text="Введите выражение:")
surname_label = Label(text="Введите точность:")
 
name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")
 
name_entry = Entry()
surname_entry = Entry()
 
name_entry.grid(row=0,column=1, padx=55, pady=35)
surname_entry.grid(row=1,column=1, padx=55, pady=35)
 
# вставка начальных данных
name_entry.insert(0, "0")
surname_entry.insert(0, "0")
 
display_button = Button(text="Рассчитать", command=display)
clear_button = Button(text="Очистить", command=clear)
 
display_button.grid(row=2, column=0, padx=15, pady=5, sticky="e")
clear_button.grid(row=2, column=1, padx=15, pady=5, sticky="e")
 
root.mainloop()

# 5! // (-12 + (-4) **2)