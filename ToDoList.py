def display_menu():
    print("\nWelcome to your To Do List!\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter a task to add to the list: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty, please try again")

def view_tasks(tasks):
    if tasks:
        print("\n--- To Do List ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("\nNo Tasks at the moment, Add some!")

def delete_task(tasks):
    if tasks:
        try:
            view_tasks(tasks)
            task_number = int(input("Enter the number of the task to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"\nTask '{removed_task}' deleted/completed successfully.")
            else:
                print("\nInvalid task number. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
    else:
        print("\nYour to-do list is empty. Nothing to delete.")

def main():
    tasks = []
    while True:
        display_menu()
        try:
            choice = input("Enter an option (1-4): ").strip()
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                delete_task(tasks)
            elif choice == "4":
                print("Thank you for using the program!")
                break
            else:
                print("Invalid Option, Please enter a number between 1 and 4.")
        except Exception as e:
            print(f"an unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

