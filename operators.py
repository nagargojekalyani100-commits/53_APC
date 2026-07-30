
# a=10
# b=10
# x=a+b
# print(x)
# 20
# a=10
# b=10
# x=a-b
# print(x)
# 0
# a=10
# b=10
# x=a*b
# print(x)
# 100
# a=10
# b=10
# x=a/b
# print(x)
# 1.0
# a=10
# b=10
# x=a//b
# print(x)
# 1
# a=10
# b=10
# x=a**b
# print(x)
# 10000000000
# a=10
# b=10
# x=a%b
# print(x)
# 0
# a=3
# a+=3
# print(a)
# 6
# a=3
# a-=2
# print(a)
# 1
# a=3
# a*=5
# print(a)
# 15
# a=3
# a/=1
# print(a)
# 3.0
# a=15
# a
# 15
# a=15
# a%=5
# print(a)
# 0
# a=15
# a//=5
# print(a)
# 3
# a**=5
# a=15
# a**=5
# print(a)
# 759375
# a=5
# >>> b=5
# >>> a==b
# True
# >>> a=5
# >>> b=5
# >>> a!=b
# False
# >>> a=5
# >>> b=10
# >>> a>b
# False
# >>> a=5
# >>> b=10
# >>> a<b
# True
# >>> a=5
# >>> b=5
# >>> a>=b
# True
# >>> a=6
# >>> b=4
# >>> a<=b
# False
# >>> a=True
# >>> b=False
# >>> a=5
# >>> b=10
# >>> a<4 & b<11
# False
# >>> a=5
# >>> b=10
# >>> a<4 or b<11
# True
# >>> a=5
# >>> b=10
# >>> a<4 not b<11
# SyntaxError: invalid syntax
# >>> a=5
# >>> b=10
# >>> not(a<4 & b<11)
# True


# n=int(input("Enter a number till you want to print:"))
# i=n
# while i<=n:
#     print(i)
#     i >>=1
#     if(i==0):
#         break;
    

import math

n = int(input("Enter the value of n: "))

sequence_sum = 0.0

for i in range(n + 1):
    sequence_sum += 1 / math.factorial(i)

print(f"The sum of the sequence up to n = {n} is: {sequence_sum}")