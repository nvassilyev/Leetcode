# https://leetcode.com/problems/longest-increasing-subsequence/

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    # Input: nums = [10,9,2,5,3,7,101,18]
    # Output: 4
    
    # brute force O(n^2)
    
    i, j = 1, 0
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[j] + 1, dp[i])
        
    return max(dp)

    # O(nlogn) solution is horrendous
        
        
    

print(lengthOfLIS([10,9,2,5,3,7,101,18,19,29]))