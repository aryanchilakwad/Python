'''
Write a function fizzbuzz(n) that takes an
integer n and prints fizz if its divisible by 3
buzz if its divisible by 5 and fizzbuzz if its divisible by both 3 and 5.
if it is not divisible by either, print the number itself.
'''

def fizzbuzz(n):
        if n%3 == 0 and n%5 ==0:
            print("fizzbuzz")
        elif n%3 ==0:
            print("fizz")
        elif n%5 ==0:
            print("buzz")
        else:
            print(n)

fizzbuzz(15)