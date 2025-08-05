todo_list = []

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"Task":task, "Status": "Pending"})
    print(" New Task Added Successfully!")

def view_tasks():
    print("Your Todo List:")
    if len(todo_list)== 0:
        print("No pending tasks!")
    else:
        for index, task in enumerate(todo_list,1):
            print(f"{index}:{task['Task']}-{task['Status']}")

def remove_task():
    if len(todo_list)==0:
        print("List is Empty!")
    else:
        try:
            search_index =int(input("Enter the task number that you want to remove:"))-1
            if 0<=search_index < len(todo_list):
               removed_task=todo_list.pop(search_index)
               print(f"Task Removed:{removed_task}")
            else:
                print("Invalid Task Number")   

        except ValueError:
              print("Invalid input. Please enter a number.")
    
def mark_done():
    if len(todo_list)==0:
        print("List is Empty!")
    else:
        try:
            search_index =int(input("Enter the task number that you want to complete:"))-1
            if 0<=search_index < len(todo_list):
                todo_list[search_index]['Status']='done'
                print(f"Task {todo_list[search_index]['Task']} has been marked as done.")
            else:
                print("Invalid Task Number")   

        except ValueError:
             print("Invalid input. Please enter a number.")
    


def menu():
    while (True):
        print("\n--- To-Do List Menu ---")
        print("1. Add a New Task")
        print("2. View  All Tasks")
        print("3. Remove a Task")
        print("4. Mark a Task as Completed ")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_done()    
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")
menu()