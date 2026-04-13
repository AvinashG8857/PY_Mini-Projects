tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet:")
    else:
        print("\n Your Tasks yet")
        for i , task in enumerate(tasks,1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def remove_task(index):
    try:
        removed = tasks.pop(index-1)
        print(f"Removed {removed}")
    except IndexError:
        print("Invalid task number")

print("||||| TO do list".upper())
while True:
    print("\n options : add or remove")
    choice = input("Enter your choice : ").lower()

    if choice=="add":
        task = input("Enter task : ")
        add_task(task)
    elif choice == "remove":
        show_tasks()
        try :
            num = int(input("Enter task nuber to remove: "))
            remove_task(num)
        except ValueError:
            print("Please enter a valid number ")
    elif choice == "show":
        show_tasks()
    elif choice == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
