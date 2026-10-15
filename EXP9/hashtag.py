import re

post = input("Enter a social media post: ")

hashtags = re.findall(r'#[A-Za-z0-9_]+', post)

print("Hashtags:", hashtags)