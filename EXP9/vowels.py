import re

string = input("Enter a string: ")

vowels = re.findall(r'[aeiouAEIOU]', string)

print("Total number of vowels:", len(vowels))