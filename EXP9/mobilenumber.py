import re

mobile = input("Enter a mobile number: ")

if re.fullmatch(r'[6-9]\d{9}', mobile):
    print("Valid Indian mobile number")
else:
    print("Invalid Indian mobile number")