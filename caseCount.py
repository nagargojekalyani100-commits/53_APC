str = input("Enter a string:")
upper =0
lower =0
for i in str :
    if i.islower():
        lower += 1
    elif i.isupper():
        upper +=1
print("upper case count:",upper)
print("lower case count",lower)
    