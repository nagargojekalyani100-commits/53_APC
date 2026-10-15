import re

text = input("Enter invoice text: ")

invoice_no = re.findall(r'Invoice\s*No\.?\s*:\s*(\w+)', text, re.IGNORECASE)
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
amounts = re.findall(r'(?:₹|Rs\.?\s*)(\d+(?:,\d{3})*(?:\.\d{2})?)', text)

print("Invoice Numbers:", invoice_no)
print("Dates:", dates)
print("Monetary Amounts:", amounts)