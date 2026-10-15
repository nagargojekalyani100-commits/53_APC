import re

paragraph = input("Enter a paragraph: ")

pin_codes = re.findall(r'\b[1-9]\d{5}\b', paragraph)

print("Indian PIN codes:", pin_codes)