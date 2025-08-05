TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = {}
    try:
        with open(TASK_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split("||")
                tasks[task] = status
    except FileNotFoundError:
        pass  
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task, status in tasks.items():
            file.write(f"{task}||{status}\n")

def show_tasks(tasks):
    if not tasks:
        print("\n No tasks in the list.\n")
    else:
        print("\n To-Do List:")
        for i, (task, status) in enumerate(tasks.items(), start=1):
            print(f"{i}. {task} - [{status}]")
        print()

def add_task(tasks):
    task = input("Enter a new task: ")
    if task in tasks:
        print(" Task already exists.")
    else:
        tasks[task] = "Pending"
        print(" Task added!")
        save_tasks(tasks)

def mark_done(tasks):
    task = input("Enter the exact task to mark as done: ")
    if task in tasks:
        tasks[task] = "Done"
        print(" Task marked as done!")
        save_tasks(tasks)
    else:
        print(" Task not found.")

def delete_task(tasks):
    task = input("Enter the exact task to delete: ")
    if task in tasks:
        del tasks[task]
        print(" Task deleted!")
        save_tasks(tasks)
    else:
        print(" Task not found.")

def main():
    tasks = load_tasks()

    while True:
        print("\n==== To-Do List Menu ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting. Tasks saved in 'tasks.txt'")
            break
        else:
            print("Invalid input. Please enter 1–5.")

if __name__ == "__main__":
    main()