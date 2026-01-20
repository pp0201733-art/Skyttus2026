tasks = []

while True:
    print("\n----- TO DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully")

    elif choice == "2":
        if not tasks:
            print("No tasks found")
        else:
            print("\nYour Task List:")
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

    elif choice == "3":
        if not tasks:
            print("No task to remove")
        else:
            num = int(input("Enter task number to delete: "))
            if num >= 1 and num <= len(tasks):
                print("Removed:", tasks.pop(num - 1))
            else:
                print("Invalid task number")

    elif choice == "4":
        tasks.clear()
        print("All tasks cleared")

    elif choice == "5":
        print("Thank you! Program closed")
        break

    else:
        print("Please enter valid option")