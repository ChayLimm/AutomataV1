import tkinter as tk
from customtkinter import *

app = CTk()
app.geometry("1080x720")

frame = CTkFrame(master=app, fg_color="#424949")
frame.pack(expand=True, fill='both')

# Adding labels, entries, and buttons in a grid layout
label1 = CTkLabel(master=frame, text="Label 1")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = CTkEntry(master=frame, placeholder_text="Type here...")
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = CTkLabel(master=frame, text="Label 2")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = CTkEntry(master=frame, placeholder_text="Type here...")
entry2.grid(row=1, column=1, padx=10, pady=10)

btn = CTkButton(master=frame, text="Submit", command=lambda: print("Button clicked"))
btn.grid(row=2, column=0, columnspan=2, pady=20)

app.mainloop()
