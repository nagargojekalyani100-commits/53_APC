#count lines,words and characters in a text file

with open("sample.txt", "w") as file:
    file.write("Hello world\n")
    file.write("Python is easy\n")
    file.write("I am learning Python\n")
with open("sample.txt", "a") as file:
    file.write("heyy kalyani here!!")

with open("sample.txt", "r") as file:
    content = file.read()

print("Number of lines:", len(content.splitlines()))
print("Number of words:", len(content.split()))
print("Number of characters:", len(content))