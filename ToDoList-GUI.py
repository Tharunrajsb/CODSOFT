import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Initialize task list and load from file
        self.tasks = []
        self.load_tasks()

        # Setup GUI components
        self.setup_gui()

    def setup_gui(self):
        """Setup GUI components."""
        self.listbox = tk.Listbox(self.root, width=50, height=15, selectmode=tk.SINGLE, bg="lightgrey")
        self.listbox.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="lightblue")
        self.add_button.pack(pady=5)

        self.mark_done_button = tk.Button(self.root, text="Mark as Done", command=self.mark_task_done, bg="lightgreen")
        self.mark_done_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, bg="salmon")
        self.delete_button.pack(pady=5)

        self.update_listbox()

    def add_task(self):
        """Add a new task."""
        title = simpledialog.askstring("New Task", "Enter task title:")
        if title:
            self.tasks.append({'title': title, 'done': False})
            self.update_listbox()
            self.save_tasks()

    def mark_task_done(self):
        """Mark a selected task as done."""
        selected_task = self.listbox.curselection()
        if selected_task:
            index = selected_task[0]
            self.tasks[index]['done'] = True
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")

    def delete_task(self):
        """Delete a selected task."""
        selected_task = self.listbox.curselection()
        if selected_task:
            index = selected_task[0]
            del self.tasks[index]
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_listbox(self):
        """Update the listbox with current tasks."""
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task['done'] else "Not Done"
            self.listbox.insert(tk.END, f"{task['title']} - {status}")

    def load_tasks(self):
        """Load tasks from the JSON file."""
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
