import tkinter as tk
from tkinter import messagebox

# 1. Define the action the button will take
def on_button_click():
    # Get the text from the entry box
    input_text = entry_box.get()

    # Update the output label
    if input_text:
        output_label.config(text=f"You entered: {input_text}")
    else:
        output_label.config(text="Please enter some text!")

# --- Main Window Setup ---
# Create the main window
root = tk.Tk()
root.title("Basic Tkinter App")
root.geometry("400x200") # Set the window size

# --- 2. Create Widgets ---

# Text Box (Entry Widget)
# Used for single-line text input
entry_box = tk.Entry(root, width=40)
# Use .pack() to place the widget in the window
entry_box.pack(pady=10) # pady adds vertical padding

# Button Widget
# Calls the 'on_button_click' function when pressed
action_button = tk.Button(
    root,
    text="Click Me",
    command=on_button_click # This is the crucial line that links the button to the function
)
action_button.pack(pady=10)

# Output Display (Label Widget)
# Used to display text output
output_label = tk.Label(root, text="Waiting for input...", fg="blue")
output_label.pack(pady=10)

# --- 3. Run the Application ---
# Start the Tkinter event loop. This line keeps the window open and responsive.
root.mainloop()