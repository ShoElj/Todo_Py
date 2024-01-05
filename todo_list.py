import tkinter as tk
from tkinter import messagebox
from datetime import datetime

tasks = []

def validate_date(date_text):
    try:
        if date_text == "Due Date (optional)" or date_text == "":
            return True  # If no due date is entered, consider it valid
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def add_task():
    task = entry_task.get()
    due_date = entry_due_date.get()
    category = combo_category.get()

    if task:
        if validate_date(due_date):
            tasks.append({"task": task, "due_date": due_date, "category": category})
            list_tasks.insert(tk.END, f"{task} - Due: {due_date if due_date else 'No due date'} - Category: {category if category else 'Uncategorized'}")
            entry_task.delete(0, tk.END)
            entry_due_date.delete(0, tk.END)
            combo_category.set("")  # Reset category selection
        else:
            messagebox.showerror("Error", "Please enter a valid date (YYYY-MM-DD format).")

root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack(padx=10, pady=10)

label_title = tk.Label(frame_tasks, text="To-Do List", font=("Arial", 18, "bold"))
label_title.pack()

list_tasks = tk.Listbox(frame_tasks, width=50, height=15, font=("Arial", 12))
list_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

list_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=list_tasks.yview)

frame_entry = tk.Frame(root)
frame_entry.pack(pady=5)

entry_task = tk.Entry(frame_entry, width=30, font=("Arial", 12))
entry_task.pack(side=tk.LEFT, padx=5)

entry_due_date = tk.Entry(frame_entry, width=15, font=("Arial", 12))
entry_due_date.pack(side=tk.LEFT, padx=5)
entry_due_date.insert(0, "Due Date (optional)")

categories = ["Work", "Personal", "Shopping", "Custom"]

combo_category = tk.StringVar()
combo_category.set("")  # Default value is an empty string
category_menu = tk.OptionMenu(frame_entry, combo_category, *categories)
category_menu.config(width=12, font=("Arial", 12))
category_menu.pack(side=tk.LEFT, padx=5)

button_add = tk.Button(frame_entry, text="Add Task", width=10, command=add_task, font=("Arial", 12, "bold"))
button_add.pack(side=tk.LEFT, padx=5)

root.mainloop()
