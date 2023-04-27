import tkinter  as tk
from tkinter import ttk

my_w = tk.Tk()
my_w.title('The Clock(V.1.5.0)')
my_w.geometry("750x515")  

from time import strftime

def my_time():
    time_string = strftime('%H:%M:%S %p \n %A \n %x')
    l1.config(text=time_string)
    l1.after(1000,my_time) 

my_font=('roman',100,'bold')

l1=tk.Label(my_w,font=my_font,bg='black',fg='red')
l1.grid(row=3,column=2,padx=25,pady=25)

my_time()
my_w.mainloop()