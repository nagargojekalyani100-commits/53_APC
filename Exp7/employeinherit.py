class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)


class Manager(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.30
        return self.basic_salary + allowance


class Developer(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.20
        return self.basic_salary + allowance


class Tester(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.15
        return self.basic_salary + allowance


# Create objects
m = Manager(101, "Rahul", 50000)
d = Developer(102, "Kalyani", 40000)
t = Tester(103, "Priya", 35000)

print("----- Manager -----")
m.display()
print("Total Salary:", m.calculate_salary())

print("\n----- Developer -----")
d.display()
print("Total Salary:", d.calculate_salary())

print("\n----- Tester -----")
t.display()
print("Total Salary:", t.calculate_salary())