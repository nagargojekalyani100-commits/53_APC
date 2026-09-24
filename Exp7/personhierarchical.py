class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.course = course

    def display_student(self):
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)


class Faculty(Person):
    def __init__(self, name, age, faculty_id, subject):
        Person.__init__(self, name, age)
        self.faculty_id = faculty_id
        self.subject = subject

    def display_faculty(self):
        print("Faculty ID:", self.faculty_id)
        print("Subject:", self.subject)


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, course, faculty_id, subject):
        Student.__init__(self, name, age, roll_no, course)
        self.faculty_id = faculty_id
        self.subject = subject

    def display(self):
        print("----- Teaching Assistant Details -----")
        self.display_person()
        self.display_student()
        self.display_faculty()


# Create object
ta = TeachingAssistant(
    "Kalyani",
    20,
    53,
    "CSE",
    201,
    "Python"
)

ta.display()