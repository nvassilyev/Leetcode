# https://leetcode.com/problems/palindrome-number/

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    for i in range(len(x)):
        if x[i] != x[len(x) - (i + 1)]:
            return False
    return True

print(isPalindrome(1221))