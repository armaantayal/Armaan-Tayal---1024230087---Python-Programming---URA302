# To-Do List Application – Project 2
tasks = []

def add_task():
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for i, t in enumerate(tasks):
            print(f"{i}: {t}")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks()
    idx = input("Enter index to delete: ")
    if not idx.isdigit():
        print("Invalid index.")
        return
    i = int(idx)
    if 0 <= i < len(tasks):
        removed = tasks.pop(i)
        print(f"Deleted: {removed}")
    else:
        print("Index out of range.")

def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
