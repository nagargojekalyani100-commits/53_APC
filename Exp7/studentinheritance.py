class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

    def display_student(self):
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)


class Result(Student):
    def __init__(self, roll_no, name, course, m1, m2, m3):
        super().__init__(roll_no, name, course)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total_marks(self):
        return self.m1 + self.m2 + self.m3

    def percentage(self):
        return self.total_marks() / 3

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display_result(self):
        self.display_student()
        print("Marks:", self.m1, self.m2, self.m3)
        print("Total Marks:", self.total_marks())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())


# Create object
r1 = Result(53, "Kalyani", "CSE", 85, 90, 80)

r1.display_result()
