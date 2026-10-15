import re

sentence = input("Enter a sentence: ")

pattern = r'\b(\w+)\s+\1\b'

words = re.findall(pattern, sentence, re.IGNORECASE)

print("Consecutive repeated words:", words)