import math
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return math.load(file)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        math.dump(tasks, file, indent=4)
def add_task(tasks):
    description = input("Enter task description: ")
    
    new_task = {
        'description': description,
        
        'completed': False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")
def view_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        print(f"{index}.  {task['description']} -  Completed: {task['completed']}")
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid task index.")
def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            print("Thank you for using the To-Do List application!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
