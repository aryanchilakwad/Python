'''
write a function tax_calculator(income) 
that takes an income as input and returns
the tax amount based on the following rules:
- If income is less than or equal to 10,000, tax is 0%
- If income is greater than 10,000 and less than or equal to 50,000, tax is 10%
- If income is greater than 50,000 and less than or equal to 100,
000, tax is 20%
- If income is greater than 100,000, tax is 30%
'''

def tax_calculator(income):
    if income <= 10000:
        tax = 0
    elif income <= 50000:
        tax = income * 0.10
    elif income <= 100000:
        tax = income * 0.20
    else:
        tax = income * 0.30
    return tax

print(tax_calculator(8000))    # Output: 0
print(tax_calculator(30000))   # Output: 3000.0