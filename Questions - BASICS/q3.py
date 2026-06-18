"""
Q3: Take the user's age as input. Check and print whether they are eligible
to vote (age >= 18) and whether they are a senior citizen (age >= 60).
Print both results.
"""

users_age = int(input("Enter your age = "))
if users_age >=18:
    print("You are eligible to vote.")
elif users_age >= 60:
    print("You are a senior citizen.")
else:
    print("You are not eligible to vote and you are not a senior citizen.")
