import re

paragraph = input("Enter student details: ")

pattern = r'Name:\s*([A-Za-z ]+),\s*Roll No:\s*(\d+),\s*Marks:\s*(\d+)'

students = re.findall(pattern, paragraph)

for student in students:
    print("Name:", student[0].strip())
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()