import re

string = input("Enter a string: ")

uppercase = re.findall(r'[A-Z]', string)

print("Uppercase letters:", uppercase)