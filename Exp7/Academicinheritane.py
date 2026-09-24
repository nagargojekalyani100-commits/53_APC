class Academic:
    def __init__(self, marks):
        self.marks = marks

    def display_marks(self):
        print("Academic Marks:", self.marks)


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points

    def display_sports_points(self):
        print("Sports Points:", self.sports_points)


class Student(Academic, Sports):
    def __init__(self, name, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)
        self.name = name

    def overall_performance(self):
        return self.marks + self.sports_points

    def display(self):
        print("Student Name:", self.name)
        self.display_marks()
        self.display_sports_points()
        print("Overall Performance:", self.overall_performance())


# Create object
s1 = Student("Kalyani", 85, 15)

s1.display()