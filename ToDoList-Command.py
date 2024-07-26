import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from a JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            status = "Done" if task['done'] else "Not Done"
            print(f"{idx}. {task['title']} - {status}")

def add_task(tasks):
    """Add a new task."""
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({'title': title, 'done': False})
        print(f"Task '{title}' added.")
    else:
        print("Task title cannot be empty.")

def mark_task_done(tasks):
    """Mark a task as done."""
    display_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['done'] = True
            print(f"Task '{tasks[index]['title']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Delete a task."""
    display_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the To-Do List application."""
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()