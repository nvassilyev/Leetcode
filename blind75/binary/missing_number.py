# https://leetcode.com/problems/missing-number/

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    # total = 0
    # for i in range(len(nums)+1):
    #     total += i
    # for n in nums:
    #     total -= n
    # return total
    
    # or (more concise)
    
    # n = len(nums)
    # return n * (n+1) / 2 - sum(nums)
    
    # bit manipulation
    
    # a ^ b ^ b = a
    
    xor = len(nums)
    for i in range(nums):
        xor ^= i ^ nums[i]
    return xor
        
    
            