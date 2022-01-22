# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    # find index of pivot
    n  = len(nums)
    l, r = 0 , n - 1
    while l < r:
        m = (l + r)//2
        if nums[m] > nums[r]:
            l = m+1
        else:
            r = m
    pivot = l
    
    #binary search but accounting for pivot
    # l, r = 0 , len(nums) - 1
    # while l <= r:
    #     m = (l + r)//2
    #     real_m = (m + pivot) % (len(nums))
    #     if nums[real_m] == target:
    #         return real_m
    #     elif nums[real_m] > target:
    #         r = m - 1
    #     else:
    #         l = m + 1
    # return -1
    
    # More intuitive:
    # Search on either left or right sublist from pivot
    if target <= nums[n-1]:
        l, r = pivot, n-1
    else:
        l, r = 0, pivot-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif target < nums[m]:
            r = m-1
        else:
            l = m+1
    return -1
     


print(search([4,5,6,7,0,1,2],0))
