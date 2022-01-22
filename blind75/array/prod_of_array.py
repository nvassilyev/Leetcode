# https://leetcode.com/problems/product-of-array-except-self/

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    prod = [1]
    for i in range(1, len(nums)):
        prod.append(prod[i-1] * nums[i-1])
    
    r = 1
    for i in range(len(nums)-1,-1,-1):
        prod[i] *= r
        r *= nums[i]
        
    return prod
