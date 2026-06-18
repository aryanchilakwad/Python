'''
Ask a int from the user
print all the sum of all the  numbers till that number 
starting from 1
'''

def sum_of_numbers(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
    print("The sum of all the numbers till",n,"is",total)

sum_of_numbers(100)