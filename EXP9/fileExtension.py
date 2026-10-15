import re

text = input("Enter filenames: ")

extensions = re.findall(r'\.([A-Za-z0-9]+)\b', text)

print("File extensions:", extensions)