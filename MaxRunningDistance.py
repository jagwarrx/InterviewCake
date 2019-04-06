def get_max_profit(stock_prices):

    # Calculate the max profit
    max_diff = stock_prices[1] - stock_prices[0]
    
    lowest = min(stock_prices[0], stock_prices[1])
    
    for i in range(2, len(stock_prices)):
        
        diff = stock_prices[i] - lowest
        if diff > max_diff:
            max_diff = diff
        
        if stock_prices[i] < lowest:
            lowest = stock_prices[i]
            
    return max_diff
