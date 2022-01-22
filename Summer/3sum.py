# https://leetcode.com/problems/3sum/

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    solution = []
    
    nums = sorted(nums)

    for k in range(len(nums)-2):
        if k > 0 and nums[k] == nums[k - 1]:
            pass
        else:
            i = k+1
            j = len(nums)-1
            target = -nums[k]
            while i < j:
                if nums[i] + nums[j] == target:
                    solution.append([nums[i], nums[j], nums[k]])
                    while i < j and nums[i] == nums[i+1]: i += 1
                    while i < j and nums[j] == nums[j-1]: j -= 1
                    i += 1
                    j -= 1            
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
    
    return solution        

print(threeSum([-1,0,1,2,-1,4]))
