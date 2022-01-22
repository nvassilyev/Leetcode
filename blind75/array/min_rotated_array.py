# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    n = len(nums)-1
    
    if nums[0] < nums[n-1]:
        return nums[0]
    
    def recursive(r, l, nums):
        m = (l+r)//2
        if nums[m-1] > nums[m]:
            return nums[m]
        elif nums[m+1] < nums[m]:
            return nums[m+1]
        else:
            print()
            if nums[0] > nums[m]:
                return recursive(r, m, nums)
            else:
                return recursive(m, l, nums)
                
    return recursive(0, n, nums)

def concise_solution(nums):
    l, r = 0, len(nums)-1
    #find pivot
    while l < r:
        m = (l+r)//2

        if nums[m] > nums[r]:
            l = m+1 #we know there is atleast one smaller number to the right
        else:
            r = m
    return nums[l]
            
                
        
            
# refresher for problem, has binary_search theme 
def binary_search(target, nums):
    min = 0
    max = len(nums)-1
    
    while min <= max:
        m = (min + max)//2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            max = m - 1
        else:
            min = m + 1
    return -1

print(findMin([10, 1, 2, 3, 9]))