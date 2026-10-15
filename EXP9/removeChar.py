import re

string = input("Enter a string: ")

result = re.sub(r'[^A-Za-z0-9 ]', '', string)

print("String after removing special characters:", result)