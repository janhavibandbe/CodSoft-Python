import tkinter as tk
from tkinter import messagebox
import random

lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
specialSymbols = "!@#$&*?"

def generate_password():
    try:
        length = int(length_entry.get())
        include_numbers = num_var.get()
        include_special_symbol = special_symbol.get()

        chars = lowerCase + upperCase

        if include_numbers == 'y':
            chars += numbers

        if include_special_symbol == 'y':
            chars += specialSymbols + specialSymbols[0]

        password = "".join(random.choice(chars) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the length.")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

num_var = tk.StringVar(value='n')
tk.Checkbutton(root, text="Include numbers?", variable=num_var, onvalue='y', offvalue='n').pack(pady=5)

special_symbol = tk.StringVar(value='n')
tk.Checkbutton(root, text="Include Special Symbols?", variable=special_symbol, onvalue='y', offvalue='n').pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=20)

password_entry = tk.Entry(root, font=('Arial', 12), width=30)
password_entry.pack(pady=10)

root.mainloop()
