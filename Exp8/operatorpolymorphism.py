class Student:
    def __init__(self, name, total_marks):
        self.name = name
        self.total_marks = total_marks

    
    def __gt__(self, other):
        return self.total_marks > other.total_marks

   
    def __lt__(self, other):
        return self.total_marks < other.total_marks



student1 = Student("Kalyani", 450)
student2 = Student("Sneha", 400)


if student1 > student2:
    print(student1.name, "has more marks than", student2.name)

if student1 < student2:
    print(student1.name, "has fewer marks than", student2.name)