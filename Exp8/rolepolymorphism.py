
class Person:
    def display_role(self):
        print("Person")



class Student(Person):
    def display_role(self):
        print("Role: Student")



class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")



class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")



student = Student()
faculty = Faculty()
administrator = Administrator()

people = [student, faculty, administrator]


for person in people:
    person.display_role()