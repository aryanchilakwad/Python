'''
Write a called called as max
that takes up three inputs
and prints the maximum number from those three inputs
'''

def max(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print("The maximum number is: ", num1)
    elif num2 > num1 and num2 > num3:
        print("The maximum number is: ", num2)
    else:
        print("The maximum number is: ", num3)

max(10, 20, 15)