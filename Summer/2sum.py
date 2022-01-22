import sys

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    i = 0
    j = len(nums) - 1
    
    nums = sorted(nums)
    
    while(i < j):
        if nums[i] + nums[j] == target:
            return [nums[i], nums[j]]
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
            
    return []

def twoSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i
    return []
    
print(twoSum2([2, 7, 11, 15], 9))

