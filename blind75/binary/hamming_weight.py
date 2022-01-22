# https://leetcode.com/problems/number-of-1-bits/

def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    
    #Solution 1: count += 1 if last digit == 1, bit shift right
    ones = 0
    while n:
        ones += n & 1
        n >>= 1
    return ones
    
    # Solution 2: count last significant 1 and set to 0
    # ex. n = ...100, n - 1 = ...011, n & (n-1) = ...000
    # ones = 0
    # while n:
    #     n &= n - 1
    #     ones += 1
    # return ones    
    
    
    
    
    
    
    