import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x300")

# Function to perform addition
def add():
    try:
        num1 = float(input_field1.get())
        num2 = float(input_field2.get())
        result = num1 + num2
        label.config(text=f"The sum is: {result}")
    except ValueError:
        label.config(text="Please enter valid numbers")

# Function to perform subtraction
def subtract():
    try:
        num1 = float(input_field1.get())
        num2 = float(input_field2.get())
        result = num1 - num2
        label.config(text=f"The difference is: {result}")
    except ValueError:
        label.config(text="Please enter valid numbers")

# Function to perform multiplication
def multiply():
    try:
        num1 = float(input_field1.get())
        num2 = float(input_field2.get())
        result = num1 * num2
        label.config(text=f"The product is: {result}")
    except ValueError:
        label.config(text="Please enter valid numbers")

# Function to perform division
def divide():
    try:
        num1 = float(input_field1.get())
        num2 = float(input_field2.get())
        if num2 != 0:
            result = num1 / num2
            label.config(text=f"The quotient is: {result}")
        else:
            label.config(text="Error: Division by zero")
    except ValueError:
        label.config(text="Please enter valid numbers")

# Input fields
input_field1 = tk.Entry(root)
input_field1.pack(pady=10)

input_field2 = tk.Entry(root)
input_field2.pack(pady=10)

# Operation buttons
button_add = tk.Button(root, text="Add", command=add)
button_add.pack(pady=5)

button_subtract = tk.Button(root, text="Subtract", command=subtract)
button_subtract.pack(pady=5)

button_multiply = tk.Button(root, text="Multiply", command=multiply)
button_multiply.pack(pady=5)

button_divide = tk.Button(root, text="Divide", command=divide)
button_divide.pack(pady=5)

# Result label
label = tk.Label(root, text="Result will be displayed here")
label.pack(pady=20)

# Run the application
root.mainloop()
