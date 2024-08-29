import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())  # Get the desired password length from user input
        if length <= 0:
            raise ValueError  
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number greater than 0 for the password length.")
        return
    
    complexity = complexity_var.get()  # Get the complexity option from user input

    if complexity == 'Low':
        chars = string.ascii_lowercase
    elif complexity == 'Medium':
        chars = string.ascii_letters + string.digits
    elif complexity == 'High':
        chars = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(chars) for _ in range(length))
    
    # Open a new window to display the password
    display_password_window(password)

def display_password_window(password):
    pw_window = tk.Toplevel(root)
    pw_window.title("Your Strong Password")
    
    tk.Label(pw_window, text="Your Strong Password is:").pack(pady=10)
    pw_entry = tk.Entry(pw_window, width=30, justify="center")
    pw_entry.pack(pady=5)
    pw_entry.insert(0, password)

    def copy_pw():
        pw_window.clipboard_clear()
        pw_window.clipboard_append(pw_entry.get())
        messagebox.showinfo("Copied", "Password copied to clipboard!")

    tk.Button(pw_window, text="Copy to Clipboard", command=copy_pw).pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
tk.Label(root, text="Password Length:").grid(row=0, column=0, pady=5)
length_entry = tk.Entry(root, justify="center")
length_entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="Complexity:").grid(row=1, column=0, pady=5)
complexity_var = tk.StringVar(value="Medium")
tk.OptionMenu(root, complexity_var, "Low", "Medium", "High").grid(row=1, column=1, pady=5)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=2, column=0, columnspan=2, pady=10)

# Start the GUI
root.mainloop()
