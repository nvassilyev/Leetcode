# https://leetcode.com/problems/string-to-integer-atoi/
import re

def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    i = total = 0
    sign = 1
    max = 2**32 - 1
    min = -(max + 1)
    
    if len(s) == 0:
        return 0
    
    while s[i] == ' ' and i < len(s) - 1:
        i += 1
    
    if s[i] == '+' or s[i] == '-' and i < len(s):
        sign = -1 if s[i] == '-' else 1
        i += 1
        
    while i < len(s):
        if not s[i].isnumeric():
            break
        total = total * 10 + int(s[i])
        i += 1
        
    total *= sign
    if total > max:
        total = max
    elif total < min:
        total = min
    return total


        

