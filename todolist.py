import os

# Function to display the to-do list
def display_tasks(tasks):
    if not tasks:
        print("No tasks to display!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Function to add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

# Function to remove a task
def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to save tasks to a file
def save_to_file(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("\nTasks saved to 'tasks.txt'.")

# Function to load tasks from a file
def load_from_file():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    return []

# Main function to control the application flow
def todo_list_app():
    tasks = load_from_file()
    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Save tasks")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        print(f"Choice entered: {choice}")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_to_file(tasks)
        elif choice == '5':
            save_to_file(tasks)
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the To-Do List Application
if __name__ == "__main__":
    todo_list_app()
