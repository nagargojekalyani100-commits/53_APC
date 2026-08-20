str = input("Enter a String:")
words = str.split()
shortest = words[0]
for word in words:
    if len(word) <  len(shortest):
        shortest = word
print("shortest word:", shortest)