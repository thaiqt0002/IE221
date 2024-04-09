class Employee:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

class ProductionEmployee(Employee):
    def __init__(self, name, birthdate, basic_salary, num_products):
        super().__init__(name, birthdate)
        self.basic_salary = basic_salary
        self.num_products = num_products

    def calculate_salary(self):
        return self.basic_salary + self.num_products * 5000

class OfficeEmployee(Employee):
    def __init__(self, name, birthdate, num_workdays):
        super().__init__(name, birthdate)
        self.num_workdays = num_workdays

    def calculate_salary(self):
        return self.num_workdays * 100000

#Ví dụ:
production_employee = ProductionEmployee("John Doe", "1990-01-01", 5000000, 100)
office_employee = OfficeEmployee("Jane Smith", "1995-05-10", 20)

print("Production Employee Salary:", production_employee.calculate_salary())
print("Office Employee Salary:", office_employee.calculate_salary())