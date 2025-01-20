import csv
import json

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description      
        self.due_date = due_date
        self.status = status
    
    def update(self, title=None, description=None, due_date=None, status=None):
        if title: self.title = title
        if description: self.description = description
        if due_date: self.due_date = due_date
        if status: self.status = status
    
    def __str__(self):
        return f"{self.task_id}: {self.title} - {self.status}"

class TaskManager:
    def __init__(self, filename, file_format):
        self.filename = filename
        self.file_format = file_format
        self.tasks = self.load_tasks()
    
    def save_tasks(self):
        if self.file_format == "json":
            with open(self.filename, 'w') as f:
                json.dump([task.__dict__ for task in self.tasks], f)
        elif self.file_format == "csv":
            with open(self.filename, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])
    
    def load_tasks(self):
        tasks = []
        try:
            if self.file_format == "json":
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    tasks = [Task(**task) for task in data]
            elif self.file_format == "csv":
                with open(self.filename, mode = 'r') as f:
                    reader = csv.reader(f)
                    next(reader)
                    for row in reader:
                        task_id, title, description, due_date, status = row
                        tasks.append(Task(task_id, title, description, due_date, status))
        except FileNotFoundError:
            pass
        return tasks

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
    
    def get_task(self, task_id):
        for task in self.tasks:
            if self.tasks == task_id:
                return task
        return None
   
    def update_task(self, task_id, **kwargs):
        task = self.get_task(task_id)
        if task:
            task.update(**kwargs)
            self.save_tasks()
   
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.save_tasks
   
    def filter_tasks(self, status):
        return [task for task in self.tasks if task.status == status]

if __name__ == "__main__":
    print("Welcome to the To-Do Application")
    print("Chooose a file format to store tasks:")
    print("1. CSV")
    print("2. JSON")
    
    file_format_choice = input("Enter 1 for CSV or anything for JSON: ").strip()
    if file_format_choice == '1':
        file_format = "csv"
        filename = "tasks.csv"
    else:
        file_format = "json"
        filename = "tasks.json"
    
    task_manager = TaskManager(filename, file_format)

    while True:
        print(
            """
            \nTo-Do application menu
            1. Add task
            2. View tasks
            3. Update task
            4. Delete task
            5. Filter task by status
            6. Exit
            """ 
        )
        choice = input("Enter your choice(1-6): ")
        
        if choice == '1':
            task_id = input("Enter task id: ")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            status = input("Enter task status (Pending, In Progress, Completed): ")
        
        elif choice == '2':
            print("\nAll tasks:")
            for task in task_manager.tasks:
                print(task)
        
        elif choice == '3':
            task_id = input("Enter task id to update: ")
            task = task_manager.get_task(task_id)
            if task:
                title = input(f"Enter new title: (current: {task.title}): ") or task.title
                description = input(f"Enter new descriptiom: (current: {task.description}): ") or task.description
                due_date = input(f"Enter new due date: (current: {task.due_date}): ") or task.due_date
                status = input(f"Enter new status: (current: {task.status}): ") or task.status
                task_manager.update_task(task_id, title=title, description=description, due_date=due_date, status=status)
                print(f"Task id {task_id} updated")
            else:
                print("Task id not found")

        elif choice == '4':
            task_id = input("Enter task id to delete")
            task_manager.delete_task(task_id)
            print(f"Task {task_id} deleted")

        elif choice == '5':
            status = input("Enter status to filter (Pending, In progress, Completed): ")
            filtered_tasks = task_manager.filter_tasks(status)
            print(task)

        elif choice == '6':
            print("Exiting")
            break

        else:
            print("Invalid choice. Enter between 1-6")             

            



        

        