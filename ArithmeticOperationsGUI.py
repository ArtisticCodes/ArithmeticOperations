import tkinter as tk

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_value_label.config(text=result)
    except ValueError:
        result_value_label.config(text="Invalid Input")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_value_label.config(text=result)
    except ValueError:
        result_value_label.config(text="Invalid Input")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_value_label.config(text=result)
    except ValueError:
        result_value_label.config(text="Invalid Input")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 != 0:
            result = num1 / num2
            result_value_label.config(text=result)
        else:
            result_value_label.config(text="∞")
    except ValueError:
        result_value_label.config(text="Invalid Input")

# Create the main window
root = tk.Tk()
root.title("Simple Arithmetic Calculator")

entry1 = tk.Entry(root, font=('Arial', 14))
entry1.pack(pady=10)

entry2 = tk.Entry(root, font=('Arial', 14))
entry2.pack(pady=10)

tk.Button(root, text="Add", command=add, font=('Arial', 14)).pack(pady=5)
tk.Button(root, text="Subtract", command=subtract, font=('Arial', 14)).pack(pady=5)
tk.Button(root, text="Multiply", command=multiply, font=('Arial', 14)).pack(pady=5)
tk.Button(root, text="Divide", command=divide, font=('Arial', 14)).pack(pady=5)

result_frame = tk.Frame(root)
result_frame.pack(pady=20)

tk.Label(result_frame, text="Result:", font=('Arial', 14)).pack(side=tk.LEFT)
result_value_label = tk.Label(result_frame, text="", font=('Arial', 14), fg="blue")
result_value_label.pack(side=tk.LEFT)

root.mainloop()
