# stock 

def stock(prices):
    min_price = prices[0]
    max_price = 0
    
    for price in prices[1:]:
        profit = price - min_price
        max_price = max(max_price, profit)
        min_price = min(min_price, price)
        
    return max_price

print(stock([7, 1, 5, 3, 6, 4]))
        