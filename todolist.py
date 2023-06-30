import pickle

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task(tasks):
    print("Current tasks:")
    view_tasks(tasks)
    index = int(input("Enter the index of the task to delete: "))
    
    if index >= 0 and index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Deleted task: {deleted_task}")
    else:
        print("Invalid index!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"{index}. {task}")

def save_tasks(tasks):
    filename = input("Enter the filename to save tasks: ")
    
    try:
        with open(filename, "wb") as file:
            pickle.dump(tasks, file)
        print("Tasks saved successfully!")
    except Exception as e:
        print(f"Error: {e}")

def load_tasks():
    filename = input("Enter the filename to load tasks: ")
    
    try:
        with open(filename, "rb") as file:
            tasks = pickle.load(file)
        print("Tasks loaded successfully!")
        return tasks
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"Error: {e}")
    
    return []

def main():
    tasks = []

    while True:
        print("\nWelcome to the To-Do List App!")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. View tasks")
        print("4. Save tasks to a file")
        print("5. Load tasks from a file")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            delete_task(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
        elif choice == "5":
            tasks = load_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
