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
    def __init__(self, name, birthdate, num_workdays = 0):
        super().__init__(name, birthdate)
        self.num_workdays = num_workdays

    def calculate_salary(self):
        return self.num_workdays * 100000

# Nhập thông tin cho ProductionEmployee
name = input("Nhập tên: ")
birthdate = input("Nhập ngày sinh: ")
basic_salary = float(input("Nhập lương cơ bản: "))
num_products = int(input("Nhập số lượng sản phẩm: "))
production_employee = ProductionEmployee(name, birthdate, basic_salary, num_products)

# Nhập thông tin cho OfficeEmployee
name = input("Enter name: ")
birthdate = input("Nhập ngày sinh: ")
num_workdays = int(input("Nhập số ngày làm việc:"))
office_employee = OfficeEmployee(name, birthdate, num_workdays)

print("Lương nhân viên sản phẩm:", production_employee.calculate_salary())
print("Lương nhân viên văn phòng:", office_employee.calculate_salary())
