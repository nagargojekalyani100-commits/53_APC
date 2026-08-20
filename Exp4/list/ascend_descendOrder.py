numbers=[]
for i in range(10):
    nums = int(input("Enter the number:"))
    numbers.append(nums)
numbers.sort()
print("ascending order:",numbers)
numbers.sort(reverse=True)
print("descending order:",numbers)

