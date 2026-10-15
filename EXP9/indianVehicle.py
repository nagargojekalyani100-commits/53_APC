import re

number = input("Enter vehicle registration number: ")

pattern = r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$'

if re.fullmatch(pattern, number):
    print("Valid vehicle registration format")
else:
    print("Invalid vehicle registration format")