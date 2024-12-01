import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive number.")
        
        include_letters = letters_var.get()
        include_numbers = numbers_var.get()
        include_specials = specials_var.get()

        if not (include_letters or include_numbers or include_specials):
            raise ValueError("At least one character type must be selected.")

        char_pool = ''
        if include_letters:
            char_pool += string.ascii_letters
        if include_numbers:
            char_pool += string.digits
        if include_specials:
            char_pool += string.punctuation

        password = ''.join(random.choice(char_pool) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
specials_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).grid(row=1, column=0, padx=5, pady=5, sticky="w")
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, column=0, padx=5, pady=5, sticky="w")
tk.Checkbutton(root, text="Include Special Characters", variable=specials_var).grid(row=3, column=0, padx=5, pady=5, sticky="w")

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

tk.Label(root, text="Generated Password:").grid(row=5, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()
