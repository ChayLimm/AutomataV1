from customtkinter import *
import tkinter
from function import *

# List to store rows of CTkEntry widgets
entries = []
fa = NONE


def onClick():
    global fa
    all_filled = True
    for row in entries:
        for entry in row:
            if not entry.get():
                error_label.configure(text="All fields must be filled.")
                all_filled = False
                break
        if not all_filled:
            break

    if all_filled:
        fa = FiniteAutomaton()
        start_state = starter[0].get()
        accept_state = starter[1].get()
        print("Start State:", start_state)
        print("Final State:", accept_state)
        
        fa.add_state(start_state, start=True)
        fa.add_state(accept_state, accept=True)
        
        for row in entries:
            from_state = row[0].get()
            to_state = row[1].get()
            symbol = row[2].get()
            print(f"State: {from_state}, TO State: {to_state}, Symbol: {symbol}")
            fa.add_transition(from_state, to_state, symbol)

        # Generate or update the image
        fa.to_graph("nfa.png")
        dfa = fa.nfa_to_dfa()
        dfa.to_graph('dfa.png')        
        update_image()
        #update deterministic
        test_derministic()
    

def update_image():
    global label
    new_image_path = "nfa.png"  # Update this with the path to the new image
    new_image = tkinter.PhotoImage(file=new_image_path)
    if label:
        label.destroy()  # Destroy the previous label if it exists
    label = CTkLabel(master=frameimg, image=new_image)
    label.image = new_image  # Keep a reference to prevent garbage collection
    label.pack()

def update_imagedfa():
    all_filled = True
    for row in entries:
        for entry in row:
            if not entry.get():
                error_label.configure(text="All fields must be filled.")
                all_filled = False
                break
        if not all_filled:
            break
    if all_filled:
        global labeldfa 
        new_image_pathdfa = "dfa.png"  # Update this with the path to the new image
        new_imagedfa = tkinter.PhotoImage(file=new_image_pathdfa)
    if labeldfa:
        labeldfa.destroy()  # Destroy the previous label if it exists
    labeldfa = CTkLabel(master=framedfa, image=new_imagedfa)
    labeldfa.image = new_imagedfa  # Keep a reference to prevent garbage collection
    labeldfa.pack()
            
count = 3
def addRow():
    global count
    print(count)
    if count >= 2+18: #2 is default
        error_label.configure(text="Row maximun 10")
        return
    else : 
       row_entries = []
       state = CTkEntry(master=frame, placeholder_text="state..")
       state.grid(row=count, column=0, padx=10, pady=10)  
       row_entries.append(state)  

       tostate = CTkEntry(master=frame, placeholder_text="to...")
       tostate.grid(row=count, column=1, padx=10, pady=10) 
       row_entries.append(tostate) 

       symbol = CTkEntry(master=frame, placeholder_text="symbol..")
       symbol.grid(row=count, column=2, padx=10, pady=10)  
       row_entries.append(symbol)  

       entries.append(row_entries)  
       count += 1




def deleteRow():
    global count
    if count > 3:   
        last_row = entries.pop()  
        for entry in last_row:
            entry.destroy()  
        count -= 1 
        print(count) 
        error_label.configure(text="")  
    else:
        error_label.configure(text="No more rows to delete.")  

def resetAll():
    global app
    app.destroy()  # Destroy the current instance of the application
    app = CTk()  # Create a new instance of the application
    app.geometry("1080x720")
    app.title("Automata")
    app.mainloop()  # Start the main loop of the application

def test_derministic():
    
    print(fa.is_deterministic())

app = CTk()
app.geometry("1080x720")
app.title("Automata")

frameBtn = CTkFrame(master=app, fg_color="#424949", height=10, width=10)
frameBtn.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Frame input
frame = CTkFrame(master=app, fg_color="#424949", height=10, width=10)
frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

#Frame image kon kam jea
frameimg = CTkFrame(master=app, fg_color="#FAF9F6", height=10, width=10)
frameimg.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")

#dfa frame
framedfa = CTkFrame(master=app, fg_color="#FAF9F6", height=10, width=10)
framedfa.grid(row=0, column=3, padx=20, pady=20, sticky="nsew")

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


labeldfa = CTkLabel(master=framedfa)

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


# Create the buttons

add_row_button = CTkButton(master=frameBtn, text="Add row", command=addRow)
add_row_button.grid(row=0, column=0, columnspan=1, pady=20)

enter_button = CTkButton(master=frameBtn, text="Enter", command=onClick)
enter_button.grid(row=2, column=0, columnspan=2, pady=20)

delete_row_button = CTkButton(master=frameBtn, text="Delete row", command=deleteRow)
delete_row_button.grid(row=1, column=0, columnspan=1, pady=20)

# Deterministic
deterministic= CTkButton(master=frameBtn, text="Test deterministic", command=test_derministic)
deterministic.grid(row=3, column=0, padx=10, pady=10, sticky='ne')

#dfa button
dfa_button = CTkButton(master=frameBtn, text="Convert to DFA", command=update_imagedfa)
dfa_button.grid(row=4, column=0, padx=10, pady=10, sticky='ne')

# Reset button
reset_button = CTkButton(master=frameBtn, text="Reset", command=resetAll)
reset_button.grid(row=5, column=0, padx=10, pady=10, sticky='ne')

# Create the error label
error_label = CTkLabel(master=frameBtn, text="", text_color="red")
error_label.grid(row=6, column=0, padx=10, pady=10)


app.mainloop()
