text = input("Enter a String: ").lower()

start = 0
end = len(text) - 1
is_palindrome = True

while start < end:
    if text[start] != text[end]:
        is_palindrome = False
        break
    start += 1
    end -= 1

if is_palindrome:
    print("String is a palindrome.")
else:
    print("String is not a palindrome.")
