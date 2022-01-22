# https://leetcode.com/problems/3sum/

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    solutions = []
    nums = sorted(nums)
    for i in range(len(nums)):
        target = -nums[i]
        l, r = i+1, len(nums)-1
        if i > 0 and nums[i] == nums[i-1]:
            pass
        else:
            while l < r:
                if nums[l] + nums[r] == target:
                    solutions.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
    return solutions

print(threeSum([-2,0,0,2,2]))