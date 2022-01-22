def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    
    solution = []
    
    nums = sorted(nums)

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i-1]:
            pass
        else:
            for j in range(i+1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    pass
                else:
                    t = target - nums[i] - nums[j]
                    lo = j+1
                    hi = len(nums)-1
                    while lo < hi:
                        if nums[lo] + nums[hi] == t:
                            solution.append([nums[i], nums[j], nums[lo], nums[hi]])
                            while lo < hi and nums[lo] == nums[lo+1]: lo += 1
                            while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
                            lo += 1
                            hi -= 1
                        elif nums[lo] + nums[hi] < t:
                            lo += 1
                        else:
                            hi -= 1
    return solution
            
print(fourSum([2,2,2,2,2], 8))