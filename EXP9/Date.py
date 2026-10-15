import re

paragraph = input("Enter a paragraph: ")

dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', paragraph)

print("Dates:", dates)