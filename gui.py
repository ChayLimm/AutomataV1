from customtkinter import *
import tkinter

app = CTk()
app.geometry("1080x720")
app.title("Automata")
# Frame for entries
frame = CTkFrame(master=app, fg_color="#424949", height=10, width=10)
frame.pack(expand=True, fill='both')

# List to store 
entries = []
state = []
tostate = []
symbol = []   


def onClick():
    for entry in entries:
        print(f"Enter value: {entry.get()}")

def addRow():
    global count 
    count += 1
    print(count)
    return count+1

    

# Create labels
label = CTkLabel(master=frame, text="State")
label.grid(row=0, column=0, padx=10, pady=10)
label1 = CTkLabel(master=frame, text="TO State")
label1.grid(row=0, column=1, padx=10, pady=10)
label2 = CTkLabel(master=frame, text="Symbol")
label2.grid(row=0, column=2, padx=10, pady=10)

# Create 3 entries

#loop to arrange grid

rowcount = addRow()

for i in range(1, rowcount):
    state = CTkEntry(master=frame, placeholder_text="state..")
    state.grid(row=i, column=0, padx=10, pady=10)  # Use grid for entries
    entries.append(state)  # Store the entry reference in the list

    tostate = CTkEntry(master=frame, placeholder_text="to...")
    tostate.grid(row=i, column=1, padx=10, pady=10)  # Use grid for entries
    entries.append(tostate)  # Store the entry reference in the list

    symbol = CTkEntry(master=frame, placeholder_text="symbol..")
    symbol.grid(row=i, column=2, padx=10, pady=10)  # Use grid for entries
    entries.append(symbol)  # Store the entry reference in the list

# Create the button

btn = CTkButton(master=frame, text="Add row", command=addRow)
btn.grid(row=i+1, column=1, columnspan=3, pady=20)  # Use grid for button


btn = CTkButton(master=frame, text="Enter", command=onClick)
btn.grid(row=i+1, column=2, columnspan=3, pady=20)  # Use grid for button

app.mainloop()
