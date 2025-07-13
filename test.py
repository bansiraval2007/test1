import os
import json
from datetime import datetime

TASKS_FILE = "tasks.json"

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at
        }

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = Task(title, description)
    tasks = load_tasks()
    tasks.append(task.to_dict())
    save_tasks(tasks)
    print("✅ Task added!")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task['completed'] else "❌"
        print(f"{idx}. [{status}] {task['title']} - {task['description']}")

def mark_complete():
    list_tasks()
    try:
        idx = int(input("Enter task number to complete: ")) - 1
        tasks = load_tasks()
        if 0 <= idx < len(tasks):
            tasks[idx]['completed'] = True
            save_tasks(tasks)
            print("🎉 Task marked as complete.")
        else:
            print("⚠️ Invalid index.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task():
    list_tasks()
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        tasks = load_tasks()
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            save_tasks(tasks)
            print("🗑️ Task deleted.")
        else:
            print("⚠️ Invalid index.")
    except ValueError:
        print("❌ Please enter a valid number.")

def show_menu():
    print("\n==== Task Manager ====")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid option.")

if __name__ == "__main__":
    main()
