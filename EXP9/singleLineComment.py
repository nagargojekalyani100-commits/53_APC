import re

code = """
x = 10  # This is a comment
# This is a single-line comment
print("Hello")
"""

comments = re.findall(r'#.*', code)

print("Single-line comments:")
for comment in comments:
    print(comment)