import re

string = "My roll number is 53 and my marks are 95"

digits = re.findall(r'\d', string)

print("Digits:", digits)