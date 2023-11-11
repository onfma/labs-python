class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        return f"Employee ID: {self.employee_id}\nName: {self.name}"

class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.salary = 80000  # Fixed salary for Manager
        self.team_size = team_size

    def display_info(self):
        return f"{super().display_info()}\nRole: Manager\nSalary: ${self.salary}\nTeam Size: {self.team_size}"

    def conduct_meeting(self):
        return f"{self.name} is conducting a meeting."

class Engineer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.salary = 70000  # Fixed salary for Engineer
        self.programming_language = programming_language

    def display_info(self):
        return f"{super().display_info()}\nRole: Engineer\nSalary: ${self.salary}\nProgramming Language: {self.programming_language}"

    def write_code(self):
        return f"{self.name} is writing code."

class Salesperson(Employee):
    def __init__(self, name, employee_id, sales_target):
        super().__init__(name, employee_id)
        self.salary = 60000  # Fixed salary for Salesperson
        self.sales_target = sales_target

    def display_info(self):
        return f"{super().display_info()}\nRole: Salesperson\nSalary: ${self.salary}\nSales Target: ${self.sales_target}"

    def make_sale(self):
        return f"{self.name} made a sale."

# Example usage:
manager = Manager("John Smith", 1001, 10)
print(manager.display_info())
print(manager.conduct_meeting())

print("\n")

engineer = Engineer("Alice Johnson", 2001, "Python")
print(engineer.display_info())
print(engineer.write_code())

print("\n")

salesperson = Salesperson("Bob Williams", 3001, 500000)
print(salesperson.display_info())
print(salesperson.make_sale())
