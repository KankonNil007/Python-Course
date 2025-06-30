# Employee Management System

# Topics: Class, Constructor, Public/Private, Inheritance

# 📝 Task:
# Employee class with public name, private salary

# Manager subclass with department

# Create a method to show details

# Use private access to prevent changing salary directly

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary.")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_details(self):
        print("Manager Details:")
        print(f"Name: {self.name}")
        print(f"Salary: {self.get_salary()}")
        print(f"Department: {self.department}")

# --- User Interaction ---
emp_name = input("Enter employee name: ")
emp_salary = int(input("Enter salary: "))
emp1 = Employee(emp_name, emp_salary)

print(f"Employee salary: {emp1.get_salary()}")

# Simulate wrong access
print("Trying to change salary to 100000...")
emp1.__salary = 100000
print(f"Salary after direct attempt: {emp1.get_salary()}")  # Still original

# Manager
mgr_name = input("Enter manager name: ")
mgr_salary = int(input("Enter salary: "))
mgr_dept = input("Enter department: ")
mgr = Manager(mgr_name, mgr_salary, mgr_dept)
mgr.show_details()
