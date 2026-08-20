str = input("Enter a String:")
temp =""
for i in str :
    if i in temp:
        print("Duplicate values:",i)
    else:
        temp += i