import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_input.get().strip()
    if task:
        task_list.insert(tk.END, task)
        task_input.delete(0, tk.END)
    else:
        messagebox.showinfo("Input Required", "Please enter a task.")

def delete_task(event=None):
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
    except IndexError:
        messagebox.showinfo("No Selection", "Please select a task to delete.")

def mark_completed():
    try:
        index = task_list.curselection()[0]
        task = task_list.get(index)
        if not task.startswith("[Done] "):
            task_list.delete(index)
            task_list.insert(index, "[Done] " + task)
    except IndexError:
        messagebox.showinfo("No Selection", "Please select a task to mark as completed.")

root = tk.Tk()
root.title("To-Do List")
root.geometry("360x400")
root.resizable(False, False)

FONT = ("Comic Sans MS", 13)

tk.Label(root, text="To-Do List", font=("Comic Sans MS", 18, "bold")).pack(pady=8)

task_input = tk.Entry(root, font=FONT)
task_input.pack(padx=10, pady=4, fill='x')

tk.Button(root, text="Add Task", font=FONT, command=add_task).pack(pady=4)

task_list = tk.Listbox(root, font=FONT, selectbackground="#c0dfff")
task_list.pack(padx=10, pady=6, expand=True, fill='both')

task_list.bind("<Delete>", delete_task)
task_list.bind("<Double-Button-1>", delete_task)

button_frame = tk.Frame(root)
button_frame.pack(pady=6)

tk.Button(button_frame, text="Mark Completed", font=FONT, width=15, command=mark_completed).pack(side='left', padx=5)
tk.Button(button_frame, text="Delete Task", font=FONT, width=15, command=delete_task).pack(side='left', padx=5)

extra_delete_btn = tk.Button(root, text="Delete Task (Extra)", font=FONT, command=delete_task)
extra_delete_btn.pack(pady=4)

root.mainloop()
