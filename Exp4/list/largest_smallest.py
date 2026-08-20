numbers=[30,40,20,50,60]
smallest =numbers[0] 
largest =numbers[0] 
for num in numbers:
    if num>largest:
        largest =num

    if num<smallest:
        smallest=num

print("largest number:",largest)
print("smallest number:",smallest)