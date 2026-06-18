"""
Ask a number from the user, and count all the factors.

Enter a number = 10
4

Enter a number = 100
9
"""

num1 = int(input("Enter a number: "))
count = 0
for i in range(1,num1+1):
    if num1 % i == 0:
        count =  count + 1
print(count)