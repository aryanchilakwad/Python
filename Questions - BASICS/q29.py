'''
Take the function as discount_price that has 
two parameters called price and discount.
The function should return the price after the discount has been applied.
'''

def discount_price(price,discount):
    discounted_price = price - (price*discount/100)
    print("The price after the discount is: ", discounted_price)

discount_price(100, 20)