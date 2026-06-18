"""
Ask a number from the user, print the multiplication table upto 10.

Enter a number = 4

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
...
...
4 x 9 = 36
4 x 10 = 40
"""

num1 = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num1} x {i} = {num1*i}")