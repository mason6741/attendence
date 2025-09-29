import tkinter as tk
from tkinter import ttk, scrolledtext  # <-- Fix: scrolledtext is now correctly imported

def submit_feedback():
    """
    Retrieves the data from the fields, prints it to the console,
    and then clears the input fields.
    """
    # 1. Get the data from the input fields
    name = name_entry.get()
    email = email_entry.get()
    # For the Text widget, we use .get('1.0', tk.END) to get all text
    feedback = feedback_text.get('1.0', tk.END).strip()

    # 2. Print the data to the console
    print("--- Feedback Submitted ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Feedback: \n{feedback}")
    print("--------------------------\n")

    # 3. Clear the input fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    # For the Text widget, we use .delete('1.0', tk.END)
    feedback_text.delete('1.0', tk.END)

# --- Application Setup ---

# Create the main window
root = tk.Tk()
root.title("Customer Feedback")
root.geometry("400x500")

# Create a main frame for padding
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill=tk.BOTH, expand=True)

# --- Widgets ---

# 1. Main Instruction Label
instruction_label = ttk.Label(
    main_frame,
    text="Please provide feedback on your experience:",
    font=('Arial', 12, 'bold')
)
instruction_label.pack(pady=(0, 15), fill='x')

# 2. Name Input
name_label = ttk.Label(main_frame, text="Your Name:")
name_label.pack(fill='x', pady=(5, 2))
name_entry = ttk.Entry(main_frame)
name_entry.pack(fill='x', pady=(0, 10))

# 3. Email Input
email_label = ttk.Label(main_frame, text="Your Email:")
email_label.pack(fill='x', pady=(5, 2))
email_entry = ttk.Entry(main_frame)
email_entry.pack(fill='x', pady=(0, 10))

# 4. Feedback Input (using ScrolledText widget for multi-line input)
feedback_label = ttk.Label(main_frame, text="Your Feedback:")
feedback_label.pack(fill='x', pady=(5, 2))

# Use scrolledtext.ScrolledText (Fix Applied)
feedback_text = scrolledtext.ScrolledText(
    main_frame,
    wrap=tk.WORD,
    width=40,
    height=10
)
feedback_text.pack(fill='both', expand=True, pady=(0, 20))

# 5. Submit Button
submit_button = ttk.Button(
    main_frame,
    text="Submit Feedback",
    command=submit_feedback # Link the button to the function
)
submit_button.pack(pady=10)

# --- Start the main loop ---
root.mainloop()
