# https://leetcode.com/problems/maximum-subarray/
# Kardane's algorithm

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_global = max_curr = nums[0]
    for i in range(1, len(nums)):
        max_curr = max(nums[i], max_curr + nums[i])
        max_global = max(max_curr, max_global)
    return max_global

# Can also ask for length of max subarray, elem of max subarray
def alternative(nums):
    max_global = max_curr = nums[0]
    curr_subarray = [nums[0]]
    max_subarray = [nums[0]]
    curr_length = 1
    length = 1
    for i in range(1, len(nums)):
        max_curr += nums[i]
        if max_curr > nums[i]:
            curr_length += 1
            curr_subarray.append(nums[i])
        else:
            max_curr = nums[i]
            curr_subarray = [nums[i]]
            curr_length = 1
            
        if max_global < max_curr:
            max_global = max_curr
            max_subarray = curr_subarray.copy()
            length = curr_length

        max_global = max(max_curr, max_global)
        
    return max_global, max_subarray, length
            
print(alternative([5,4,-1,7,8]))