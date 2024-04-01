import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

def list_files_alphabetically(path):
    """List files and folders in alphabetical order."""
    items = os.listdir(path)
    items.sort()
    return items

def list_files_by_date(path):
    """List files and folders by date."""
    items = os.listdir(path)
    items.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)))
    return items

def list_files_by_type(path):
    """List files and folders by type."""
    items = os.listdir(path)
    items.sort(key=lambda x: (os.path.isdir(os.path.join(path, x)), x))
    return items

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        update_file_list(directory)

def update_file_list(directory):
    file_list.delete(0, tk.END)
    choice = sort_choice.get()
    if choice == 1:
        items = list_files_alphabetically(directory)
    elif choice == 2:
        items = list_files_by_date(directory)
    elif choice == 3:
        items = list_files_by_type(directory)
    else:
        messagebox.showerror("Error", "Invalid choice.")
        return

    for item in items:
        file_list.insert(tk.END, item)

root = tk.Tk()
root.title("File Manager")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

sort_choice = tk.IntVar()
sort_choice.set(1)

tk.Radiobutton(frame, text="Order alphabetically", variable=sort_choice, value=1).pack(anchor=tk.W)
tk.Radiobutton(frame, text="Order by date", variable=sort_choice, value=2).pack(anchor=tk.W)
tk.Radiobutton(frame, text="Order by type", variable=sort_choice, value=3).pack(anchor=tk.W)

browse_button = tk.Button(frame, text="Browse", command=browse_directory)
browse_button.pack(pady=5)

file_list = tk.Listbox(root, width=50, height=20)
file_list.pack(padx=10, pady=10)

root.mainloop()
