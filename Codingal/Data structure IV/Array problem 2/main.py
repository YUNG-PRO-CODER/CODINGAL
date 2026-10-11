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

#profit accumalation


def total_profit(n):
    prices = [1, n, 1, n, 1]
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


print(total_profit(4))  
print(total_profit(4))  
