x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))

sum = 1
sign = -1

for i in range(2, n + 1, 2):
    fact = 1

    # Calculate i!
    for j in range(1, i + 1):
        fact = fact * j

    # Add the term
    sum = sum + sign * (x ** i) / fact

    # Change the sign (+/-)
    sign = sign * -1

print("Cos(x) =", sum)