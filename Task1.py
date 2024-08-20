# Task - 1

# A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. This project aims to create a command-line or GUI-based application using Python, allowing users to create, update, and track their to-do lists

import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        self.root.config(bg="#2E3B55")

        self.tasks = []

        self.title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
        self.task_font = tkfont.Font(family="Helvetica", size=12)
        self.button_font = tkfont.Font(family="Helvetica", size=10, weight="bold")

        self.title_label = tk.Label(self.root, text="My To-Do List", bg="#2E3B55", fg="#FFFFFF", font=self.title_font)
        self.title_label.pack(pady=10)

        self.frame = tk.Frame(self.root, bg="#2E3B55")
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, height=10, width=30, bg="#FFFFFF", fg="#000000", selectbackground="#6FA3EF", selectforeground="#FFFFFF", font=self.task_font, bd=0)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10))

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(self.root, width=30, font=self.task_font, bg="#F5F5F5", fg="#000000", bd=0, highlightthickness=2, highlightbackground="#6FA3EF")
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(self.root, bg="#2E3B55")
        self.button_frame.pack(pady=20)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task, bg="#6FA3EF", fg="#FFFFFF", font=self.button_font, bd=0, padx=10, pady=5)
        self.add_button.grid(row=0, column=0, padx=5)

        self.remove_button = tk.Button(self.button_frame, text="Remove Task", command=self.remove_task, bg="#E27D60", fg="#FFFFFF", font=self.button_font, bd=0, padx=10, pady=5)
        self.remove_button.grid(row=0, column=1, padx=5)

        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task, bg="#85DCB0", fg="#FFFFFF", font=self.button_font, bd=0, padx=10, pady=5)
        self.update_button.grid(row=0, column=2, padx=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.entry.get()
            if new_task != "":
                self.tasks[selected_task_index[0]] = new_task
                self.update_task_listbox()
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new task.")
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
