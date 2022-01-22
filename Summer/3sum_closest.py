def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    nums = sorted(nums)
    closest = nums[0] + nums[1] + nums[-1]
    for i in range(len(nums) - 2):
        lo = i + 1
        hi = len(nums) -1 
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum > target:
                hi -= 1
            else:
                lo += 1    
            if abs(target - sum) < abs(target - closest):
                closest = sum 
    return closest

print(threeSumClosest([-1,2,1,-4], 1))