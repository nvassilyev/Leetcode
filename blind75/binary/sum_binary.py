# https://leetcode.com/problems/sum-of-two-integers/

def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """

    while b != 0:
        a = (a ^ b)   #sum
        b = ((a & b) << 1)   #carry
    return a

print(getSum(-3, 8)) #doesn't work for negatives