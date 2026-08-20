lst=[3,4,5,6,7,3,3,8,7,4]
unique =[]
for i in lst:
    if i  not in unique:
        unique.append(i)

print("Unique elements:",unique)