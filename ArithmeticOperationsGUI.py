import tkinter as tk

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
    
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 != 0:
            
            result_label.config(text=f"Result: {result}")
        else:
            result_label.config(text="Cannot divide by zero.")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Arithmetic Calculator")

# Entry for the first number
entry1 = tk.Entry(root, font=('Arial', 14))
entry1.pack(pady=10)

# Entry for the second number
entry2 = tk.Entry(root, font=('Arial', 14))
entry2.pack(pady=10)

# Addition button
add_button = tk.Button(root, text="Add", command=add, font=('Arial', 14))
add_button.pack(pady=5)

# Subtraction button
subtract_button = tk.Button(root, text="Subtract", command=subtract, font=('Arial', 14))
subtract_button.pack(pady=5)

# Multiplication button
multiply_button = tk.Button(root, text="Multiply", command=multiply, font=('Arial', 14))
multiply_button.pack(pady=5)

# Division button
divide_button = tk.Button(root, text="Divide", command=divide, font=('Arial', 14))
divide_button.pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="Result: ", font=('Arial', 14))
result_label.pack(pady=20)

# Run the main loop
root.mainloop()
