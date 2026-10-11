
def total_profit(n):
    prices = [1, n, 1, n, 1]
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


print(total_profit(4))  
print(total_profit(4))  