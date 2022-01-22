# https://leetcode.com/problems/maximum-product-subarray/

def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    cur_min = cur_max = 1
    solution = nums[0]

    # Keep track of both subarray with min product and subarray with max product
    
    for n in nums:
        val = (n, cur_max * n, cur_min * n)
        cur_min, cur_max = min(val), max(val)
        solution = max(cur_max, solution)
        
    return solution
