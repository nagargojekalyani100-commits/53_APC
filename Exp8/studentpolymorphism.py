
class Student:
    def calculate_grade(self, marks):
        print("Calculating grade")



class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 40:
            return "C"
        else:
            return "F"


class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 85:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "F"



class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 75:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 40:
            return "C"
        else:
            return "F"



engineering = EngineeringStudent()
medical = MedicalStudent()
management = ManagementStudent()


students = [
    (engineering, 75),
    (medical, 80),
    (management, 70)
]

for student, marks in students:
    print("Grade:", student.calculate_grade(marks))