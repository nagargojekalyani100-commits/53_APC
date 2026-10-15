import re

text = input("Enter a text: ")

urls = re.findall(r'https?://\S+', text)

print("Web addresses:", urls)