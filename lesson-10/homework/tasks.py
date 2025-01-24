import json
import csv

JSON_file = "tasks.json"
CSV_file = "tasks.csv"

def load_tasks(json_file):
    try:
        with open(json_file, 'r') as f:
            tasks = json.load(f)
            return tasks
    except FileNotFoundError:
        print(f"File {json_file} not found")
        return []
    
def display_tasks(tasks):
    print("\nAll tasks:")
    print(f"{'ID':<5} {'Task Name':<20} {'Completed':<10} {'Priority':<8}")
    for task in tasks:
        print(f"{task['id']:<5} {task['task']:<20} {task['completed']:<10} {task['priority']:<8}")

def save_tasks(json_file, tasks):
    with open(json_file, 'w') as f:
        json.dump(tasks, f, indent=4)
    print(f"Tasks saved to {json_file}")

def calculate_statistics(tasks):
    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task['completed']])
    incomplete_tasks = total_tasks - completed_tasks
    average_priority = sum([task['priority'] for task in tasks]) / total_tasks
    print(f"\nTotal tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Incomplete tasks: {incomplete_tasks}")
    print(f"Average priority: {average_priority:.2f}")

def write_tasks_csv(csv_file, tasks):
    with open(csv_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Task Name", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print(f"Tasks written to {csv_file}")

if __name__ == "__main__":
    initial_tasks = [
        {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
        {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
        {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
    ]
    try:
        with open(JSON_file, 'w') as f:
            json.dump(initial_tasks, f, indent=4)
    except FileExistsError:
        print(f"File {JSON_file} already exists")
    tasks = load_tasks(JSON_file)
    display_tasks(tasks)
    calculate_statistics(tasks)
    save_tasks(JSON_file, tasks)
    write_tasks_csv(CSV_file, tasks)    

     
    
