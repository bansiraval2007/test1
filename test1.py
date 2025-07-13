import json
import os
import sys
from datetime import datetime

DATA_FILE = "todo_data.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    task = {
        "description": description,
        "created": datetime.now().isoformat(),
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")

def list_tasks(show_all=False):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✖"
        if not show_all and task["completed"]:
            continue
        print(f"{idx+1}. [{status}] {task['description']}")

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print(f"Task #{index+1} marked as complete.")
    else:
        print("Invalid task index.")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['description']}")
    else:
        print("Invalid task index.")

def show_help():
    print("""
To-Do List Manager
-------------------
Usage:
    python todo.py add "Task description"
    python todo.py list
    python todo.py list --all
    python todo.py done <task number>
    python todo.py delete <task number>
""")

def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) >= 3:
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "list":
        show_all = "--all" in sys.argv
        list_tasks(show_all)
    elif command == "done" and len(sys.argv) == 3:
        try:
            index = int(sys.argv[2]) - 1
            complete_task(index)
        except ValueError:
            print("Please enter a valid task number.")
    elif command == "delete" and len(sys.argv) == 3:
        try:
            index = int(sys.argv[2]) - 1
            delete_task(index)
        except ValueError:
            print("Please enter a valid task number.")
    else:
        show_help()

if __name__ == "__main__":
    main()
