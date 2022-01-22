# https://leetcode.com/problems/roman-to-integer/

roman = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000
}

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    sum = i = 0
    while i < len(s):
        if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            sum += roman[s[i+1]] - roman[s[i]]    
            i += 2
        else:
            sum += roman[s[i]]
            i += 1
    return sum

print(romanToInt("III"))