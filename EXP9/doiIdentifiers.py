import re

text = input("Enter research paper references: ")

# Extract DOI identifiers
dois = re.findall(r'\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b', text, re.IGNORECASE)

# Extract publication years
years = re.findall(r'\b(?:19|20)\d{2}\b', text)

# Extract email addresses
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)

# Extract URLs
urls = re.findall(r'https?://[^\s]+', text)

print("DOI Identifiers:", dois)
print("Publication Years:", years)
print("Email Addresses:", emails)
print("URLs:", urls)