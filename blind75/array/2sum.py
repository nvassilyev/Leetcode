# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    d = {}

    for i, num in enumerate(nums):
        m = target - num
        if m in d:
            return [d[m], i]
        else:
            d[num] = i
            


    
    
    