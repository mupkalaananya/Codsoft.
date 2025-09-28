# Simple To-Do List in Python (Command-line)

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet.")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")

def add_task():
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print(f"Added: {title}")
    else:
        print("Task cannot be empty.")

def mark_done():
    show_tasks()
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"Marked as done: {tasks[index]['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1–5.")

if __name__ == "__main__":
    main()
