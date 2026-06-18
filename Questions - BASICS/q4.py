"""
Q4: A student scored marks in 3 subjects. Take all three as input,
calculate the total and average, and print both using an f-string.
"""

marks1 = int(input("Enter your marks in subject 1 = "))
marks2 = int(input("Enter your marks in subject 2 = "))
marks3 = int(input("Enter your marks in subject 3 = "))

total_marks = marks1 + marks2 + marks3
average_marks = total_marks / 3

print(f"Total marks = {total_marks} and Average marks = {average_marks}")
