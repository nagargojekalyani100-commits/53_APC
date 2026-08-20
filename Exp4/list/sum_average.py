numbers =[]

for i in range(10):
    num=int(input("Enter the number:"))
    numbers.append(num)

total = sum(numbers)
avg = total/len(numbers)

print("list",numbers)
print("sum:",total)
print("average",avg)
