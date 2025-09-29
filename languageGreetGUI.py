import tkinter as tk

# Define a dictionary to store the greetings
GREETINGS = {
    "English": "Hello! Welcome.",
    "Español": "¡Hola! Bienvenido/a.",
    "Français": "Bonjour ! Bienvenue.",
    "Deutsch": "Hallo! Willkommen."
}

def translate_greeting(language):
    """
    Function to update the output label with the greeting 
    corresponding to the selected language.
    """
    greeting = GREETINGS.get(language, "Language not found.")
    
    # Update the text of the output_label
    output_label.config(text=greeting, fg="darkgreen")

# --- Main Window Setup ---
root = tk.Tk()
root.title("Language Greeting Translator (Column Layout)")
root.geometry("400x350") # Adjust size for the column layout

# --- Header Label ---
header_label = tk.Label(
    root, 
    text="Select a language to see the greeting:", 
    font=("Arial", 12, "bold")
)
header_label.pack(pady=15)

# --- Button Frame ---
# A Frame is a container to hold the buttons.
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# --- Create Language Buttons (In a Column) ---
for lang in GREETINGS.keys():
    # Use a lambda function to pass the specific 'lang' argument to the function.
    tk.Button(
        button_frame,
        text=lang,
        command=lambda l=lang: translate_greeting(l),
        width=15, # Increased width for better column appearance
        height=1,
        bg="#e0e0e0"
    ).pack(fill=tk.X, pady=3) # **Change is here:** .pack(fill=tk.X, pady=3) 
                             # 'fill=tk.X' makes all buttons stretch to the same width
                             # 'pady=3' adds vertical space between buttons
                             # By default, .pack() stacks widgets from TOP to BOTTOM

# --- Output Display (Label Widget) ---
output_label = tk.Label(
    root, 
    text="Greeting will appear here...", 
    font=("Arial", 14), 
    wraplength=350
)
output_label.pack(pady=30)

# --- Run the Application ---
root.mainloop()
