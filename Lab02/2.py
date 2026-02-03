class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, hourly_rate):
        super().__init__(name, emp_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


emp1 = FullTimeEmployee("Ali", 1, 50000)
emp2 = PartTimeEmployee("Sara", 2, 80, 200)

print("Full Time Employee:")
print("Name:", emp1.name)
print("Salary:", emp1.calculate_salary())
print()

print("Part Time Employee:")
print("Name:", emp2.name)
print("Salary:", emp2.calculate_salary())
