from customtkinter import *
import tkinter
from function import *

app = CTk()
app.geometry("1080x720")
app.title("Automata")

# Frame for entries
frame = CTkFrame(master=app, fg_color="#424949", height=10, width=10)
frame.pack(expand=True, fill='both')


# List to store rows of CTkEntry widgets
entries = []

def onClick():
    all_filled = True
    for row in entries:
        for entry in row:
            if not entry.get():
                error_label.configure(text="Form must be filled")
                all_filled = False
                break
        if not all_filled:
            break
    
    if all_filled:
        error_label.configure(text="")
        print("Start Data:", starter[0].get())
        print("Final: ", starter[1].get())
        for row in entries:
            print(f"State: {row[0].get()}, TO State: {row[1].get()}, Symbol: {row[2].get()}")


            
count = 2
def addRow():
    global count
    count += 1
    print(count)
    if count >= 12:
        error_label.configure(text="Row maximun 10")
        return
    else : 
       row_entries = []
       state = CTkEntry(master=frame, placeholder_text="state..")
       state.grid(row=count, column=0, padx=10, pady=10)  # Use grid for entries
       row_entries.append(state)  # Store the entry reference in the list

       tostate = CTkEntry(master=frame, placeholder_text="to...")
       tostate.grid(row=count, column=1, padx=10, pady=10)  # Use grid for entries
       row_entries.append(tostate)  # Store the entry reference in the list

       symbol = CTkEntry(master=frame, placeholder_text="symbol..")
       symbol.grid(row=count, column=2, padx=10, pady=10)  # Use grid for entries
       row_entries.append(symbol)  # Store the entry reference in the list

       entries.append(row_entries)  # Add the row of entries to the main list

#this is the starting of the app

start_final_frame = CTkFrame(master=frame, border_color="black", width=200)
start_final_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

starter = []
label3 = CTkLabel(master=start_final_frame, text="Start/Final :")
label3.grid(row=0, column=0, padx=30, pady=10)
start = CTkEntry(master=start_final_frame, placeholder_text="start..")
start.grid(row=0, column=1, padx=30, pady=10)
starter.append(start)

# label4 = CTkLabel(master=frame, text="Final")
# label4.grid(row=0, column=2, padx=10, pady=10)
final = CTkEntry(master=start_final_frame, placeholder_text="final..")
final.grid(row=0, column=2, padx=10, pady=10)
starter.append(final)


# Create labels
label = CTkLabel(master=frame, text="State")
label.grid(row=1, column=0, padx=10, pady=10)
label1 = CTkLabel(master=frame, text="TO State")
label1.grid(row=1, column=1, padx=10, pady=10)
label2 = CTkLabel(master=frame, text="Symbol")
label2.grid(row=1, column=2, padx=10, pady=10)



# Create initial set of entry widgets
initial_row = []

state = CTkEntry(master=frame, placeholder_text="state..")
state.grid(row=2, column=0, padx=10, pady=10)
initial_row.append(state)

tostate = CTkEntry(master=frame, placeholder_text="to...")
tostate.grid(row=2, column=1, padx=10, pady=10)
initial_row.append(tostate)

symbol = CTkEntry(master=frame, placeholder_text="symbol..")
symbol.grid(row=2, column=2, padx=10, pady=10)
initial_row.append(symbol)

entries.append(initial_row)

# Create the error label
error_label = CTkLabel(master=frame, text="", text_color="red")
error_label.grid(row=11, column=0, padx=10, pady=10)
# Create the buttons

add_row_button = CTkButton(master=frame, text="Add row", command=addRow)
add_row_button.grid(row=11, column=1, columnspan=1, pady=20)

enter_button = CTkButton(master=frame, text="Enter", command=onClick)
enter_button.grid(row=11, column=2, columnspan=2, pady=20)

app.mainloop()
