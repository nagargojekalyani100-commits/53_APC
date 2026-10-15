import re

text = input("Enter a string: ")

result = re.sub(r' +', ' ', text)

print("After replacing spaces:", result)