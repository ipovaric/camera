import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry('200x100')

button = ttk.Button(
    window,
    text='Run Camera',
    width = 25)
button.pack()
window.mainloop()