class StudentResult:
    
    def __init__(self, name, m1, m2, m3, m4, m5):
        self.name = name
        self.marks = [m1, m2, m3, m4, m5]

    
    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return self.calculate_total() / 5

   
    def calculate_grade(self):
        percentage = self.calculate_percentage()

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

    
    def __del__(self):
        print("Student result object is destroyed.")



s1 = StudentResult("Kalyani", 85, 90, 78, 88, 92)

print("Student Name:", s1.name)
print("Total Marks:", s1.calculate_total())
print("Percentage:", s1.calculate_percentage())
print("Grade:", s1.calculate_grade())