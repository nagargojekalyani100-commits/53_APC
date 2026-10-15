import re

text = input("Enter a text: ")

# Remove HTML tags
text = re.sub(r'<[^>]+>', '', text)

# Remove unwanted punctuation
text = re.sub(r'[^\w\s.,!?]', '', text)

# Replace extra whitespace with a single space
text = re.sub(r'\s+', ' ', text).strip()

print("Cleaned text:", text)