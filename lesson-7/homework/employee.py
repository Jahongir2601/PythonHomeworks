class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"
class EmployeeManager:
    def __init__(self, filename = "employees.txt"):
        self.filename = filename
    def add_employee(self, employee):
        with open(self.filename, 'a') as f:
            f.write(str(employee) + "\n")
    def view_all_employees(self):
        try:
            with open(self.filename, 'r') as f:
                lines = f.readlines()
                if not lines:
                    print("There is no employee")
                else:
                    print("All employee records")
                    for line in lines:
                        print(line.strip())       
        except FileNotFoundError:
            print("The file does not exist")
    def search_employee(self, employee_id):
        try:
            with open(self.filename, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if employee_id == int(line.strip().split(", ")[0]):
                        print(f"Employee: {line.strip()}")
                        return
                print("Employee not found")
        except FileNotFoundError:
            print("There is no such employee")
    def update_employee(self, employee_id, name=None, position=None, salary=None):
        try:
            with open(self.filename, 'r') as f:
                lines = f.readlines()
            updated = False
            with open(self.filename, 'w') as f:
                for line in lines:
                    data = line.strip().split(", ")
                    if int(data[0]) == employee_id:
                        if name:
                            data[1] = name
                        if position:
                            data[2] = position
                        if salary:
                            data[3] = salary
                        f.write(", ".join(data) + "\n")
                    if updated:
                        print("Employee updated succesfully")
                    else:
                        print("Employee not found")
        except FileNotFoundError:
            print("File not found")
    def delete_employee(self, employee_id):
        try:
            with open(self.filename, 'r') as f:
                lines = f.readlines()
            with open(self.filename, 'w') as f:
                deleted = False
                for line in lines:
                    data = line.strip().split(", ")
                    if employee_id == int(data[0]):
                        deleted = True
                        print("Employee deleted")
                    else:
                        f.write(line)
                if not deleted:
                    print("Employee not found")
        except FileNotFoundError:
            print("File not found")
    def menu(self):
        while True:
            print("\nEmployee records manager")
            print("1. Add new employee")
            print("2. View all employees")
            print("3. Search an employee")
            print("4. Update an employee")
            print("5. Delete an employee")
            print("6. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_new_employee()
            elif choice == '2':
                self.view_all_employees()
            elif choice == '3':
                employee_id = int(input("Enter an employee id"))
                self.search_employee(employee_id)
            elif choice == '4':
                self.update_employee_info()
            elif choice == '5':
                self.delete_employee_record()
            elif choice == '6':
                print("Exiting")
                break
            else:
                print("Invalid option. Try again")
    def add_new_employee(self):
        try:
            employee_id = int(input("Enter employee id"))
            name = input("Enter employee name")
            position = input("Enter employee position")
            salary = float(input("Enter employee salary"))
            employee = Employee(employee_id, name, position, salary)
            self.add_employee(employee)
            print("Employee added")
        except ValueError:
            print("Enter correct data types")
    def update_employee_info(self):
        try:
            employee_id = int(input("Enter employee id to update"))
            name = input("Enter new name (leave blank to keep old)")
            position = input("Enter new position (leave blank to keep old)")
            salary_0 = input("Enter new salary (leave blank to keep old)")
            salary = None
            if  salary_0:
                salary = float(salary_0)
            self.update_employee(employee_id, name or None, position or None, salary)
        except ValueError:
            print("Enter correct data types")
    def delete_employee_info(self):
        try:
            employee_id = int(input("Enter employee id to delete"))
            self.delete_employee(employee_id)
        except ValueError:
            print("Enter correct data types")

if __name__ == "__main__":
    start = EmployeeManager()
    start.menu()