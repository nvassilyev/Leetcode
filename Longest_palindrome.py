# https://leetcode.com/problems/longest-palindromic-substring/
from typing import List

def longestPalindrome(s: str) -> str:
    """
    :type s: str
    :rtype: str
    """
    if len(s) < 2:
        return s
    
    begin = newLength = maxLength = 0

    for i in range(len(s)):
        k = j = i
        
        while k < len(s) - 1 and s[k] == s[k + 1]:
            k += 1
        while 0 < j and k < len(s) - 1 and s[j-1] == s[k+1]:
            j -= 1
            k += 1
            
        newLength = k - j + 1
        if newLength > maxLength:
            maxLength = newLength
            begin = j
        
    return s[begin : begin + maxLength]
        
    
print(longestPalindrome("a"))