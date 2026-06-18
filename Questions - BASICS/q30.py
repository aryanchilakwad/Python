'''
Return true if my number is true
and return false if my number is false
'''

def is_prime(n1):
    count = 0
    for i in range(1,n1+1):
        if n1 % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
    
print(is_prime(7))

