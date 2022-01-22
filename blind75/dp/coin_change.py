# https://leetcode.com/problems/coin-change/

def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    
    # Input: coins = [1,2,5], amount = 11
    # Output: 3
    # Explanation: 11 = 5 + 5 + 1
    
    # DP solution
    # Store min amount of coins for each value <= amount
    # Logic: for amount = i, subtract first coin -> amount = i - c
    # Since i - c < i, we have min # of coins for this amount 
    # do this for each coin smaller than amount i
    # update rule: dp[i] = min(dp[i], dp[i - c] + 1) 
    # Note: we add 1 to account for the subtracted coin since 
    # dp[i - c] gives us coins for amount i - c, and i - c + c = i = amount
    
    # value stored in dp array signifying we have not found the # of coins
    bound = amount + 1 
    
    dp = [0] + [bound] * amount
    
    for i in range(1, amount+1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)
    
    return dp[amount] if dp[amount] < bound else -1

    
    