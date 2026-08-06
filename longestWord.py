str = input("Enter a String:")
words = str.split()
longest = words[0]
for word in words:
    if len(word)> len(longest):
        longest = word
print("Longest word:",longest)