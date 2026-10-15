import re

password = input("Enter a password: ")

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9\s])\S{8,}$'

if re.fullmatch(pattern, password):
    print("Valid password")
else:
    print("Invalid password")