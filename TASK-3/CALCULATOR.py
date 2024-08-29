import tkinter as tk
from tkinter import messagebox
import math

# Function to validate inputs
def validate_inputs():
    try:
        num1 = float(entry_num1.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the first input!")
        return False
    
    if operation_var.get() != "Square Root":
        try:
            num2 = float(entry_num2.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the second input!")
            return False

    return True

# Function to perform the calculation and show result in a separate window
def calculate():
    if not validate_inputs():
        return

    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get()) if entry_num2.get() else None
    operation = operation_var.get()

    if operation == "Add":
        result = num1 + num2
        result_text = f"{num1} + {num2} = {result}"
    elif operation == "Subtract":
        result = num1 - num2
        result_text = f"{num1} - {num2} = {result}"
    elif operation == "Multiply":
        result = num1 * num2
        result_text = f"{num1} * {num2} = {result}"
    elif operation == "Divide":
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero!")
            return
        result = num1 / num2
        result_text = f"{num1} / {num2} = {result}"
    elif operation == "Square Root":
        if num1 < 0 or (num2 is not None and num2 < 0):
            messagebox.showerror("Error", "Cannot take the square root of a negative number!")
            return
        result_text = f"Square root of {num1} = {math.sqrt(num1)}"
        if num2 is not None:
            result_text += f"\nSquare root of {num2} = {math.sqrt(num2)}"
    elif operation == "Percentage":
        result = (num1 * 100) / num2
        result_text = f"{num1} * 100 / {num2} = {result}"
    elif operation == "Remainder":
        result = num1 % num2
        result_text = f"{num1} % {num2} = {result}"
    elif operation == "Power":
        result = num1 ** num2
        result_text = f"{num1} ^ {num2} = {result}"
    else:
        messagebox.showerror("Error", "Invalid operation!")
        return
    
    show_result(result_text)

# Function to display the result in a separate window
def show_result(result_text):
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    tk.Label(result_window, text=result_text, font=("Helvetica", 14)).pack(padx=10, pady=10)
    tk.Button(result_window, text="Close", command=result_window.destroy).pack(pady=5)

# Function to reset the input fields
def reset():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    operation_var.set("Select Operation")

# Create the main window
root = tk.Tk()
root.title("Enhanced Calculator")

# Create and place the widgets
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root, justify='center')
entry_num1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root, justify='center')
entry_num2.grid(row=1, column=1, padx=10, pady=5)

operation_var = tk.StringVar(root)
operation_var.set("Select Operation")
operation_menu = tk.OptionMenu(root, operation_var, 
                               "Add", "Subtract", "Multiply", "Divide", 
                               "Square Root", "Percentage", "Remainder", "Power")
operation_menu.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Reset", command=reset).grid(row=3, column=1, padx=10, pady=5)

# Start the GUI
root.mainloop()
