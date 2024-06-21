import customtkinter as ctk

def check_entry():
    if not state.get():
        error_label.configure(text="Form must be filled")
    else:
        error_label.configure(text="")  # Clear the error message
        print("Submission accepted.")  # Replace this with actual submission logic

# Initialize the main application window
root = ctk.CTk()

# Create a frame
frame = ctk.CTkFrame(master=root)
frame.pack(padx=20, pady=20)

# Create the entry widget
state = ctk.CTkEntry(master=frame, placeholder_text="state..")
state.pack(pady=10)

# Create an error label to display messages
error_label = ctk.CTkLabel(master=frame, text="", text_color="red")
error_label.pack(pady=10)

# Create a submit button
submit_button = ctk.CTkButton(master=frame, text="Submit", command=check_entry)
submit_button.pack(pady=10)

# Start the main event loop
root.mainloop()
