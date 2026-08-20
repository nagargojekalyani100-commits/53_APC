n = int(input("Enter a range:"))
for i in range(n+1):
    number = 1 << i
    print(number, end =" ")
    if number>n:
        break