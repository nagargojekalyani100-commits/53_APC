class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Monthly Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_manager(self):
        self.display_employee()
        print("Department:", self.department)

    def annual_salary(self):
        return self.salary * 12


# Create Employee object
e1 = Employee(101, "Rahul", 30000)

# Create Manager object
m1 = Manager(102, "Kalyani", 50000, "IT")

print("----- Employee Details -----")
e1.display_employee()

print("\n----- Manager Details -----")
m1.display_manager()
print("Manager's Annual Salary:", m1.annual_salary())