"""
Q6: Take two numbers as input. Print the greater of the two. If they are
equal, print "Both are equal."
"""

num1 = int(input("Enter the first number = "))
num2 = int(input("Enter the second number = "))

if num1 > num2 :
    print("Number 1 is greater than number 2")
elif num2 > num1 :
    print("Number 2 is greater than number 1")
else:
    print("Both are equal.")