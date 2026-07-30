m1 = int(input("Enter marks of subject 1:"))
m2 = int(input("Enter marks of subject 2:"))
m3 = int(input("Enter marks of subject 3:"))
per = int(m1+m2+m3)/3
print(per)
if (per>=90):
    print("Excellent performance!")
elif(per>=80):
    print("Very good performance!")
elif(per>=70):
    print("Good performance!")
elif(per>=60):
    print("Average performance!")
else:
    print("poor performance!")