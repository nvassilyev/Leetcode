# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

def kadanes_algo(prices):
    # Ex: for {1, 7, 4, 11}, we have differences {0, 6, -3, 7}
    curr_max, global_max = 0, 0
    for i in range(1, len(prices)):
        curr_max = max(0, curr_max + prices[i] - prices[i-1])
        global_max = max(curr_max, global_max)
    return global_max
        

