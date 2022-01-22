# https://leetcode.com/problems/counting-bits/

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    
    """
    101010101010
    -----------  (1)
    101010101010
               - (2)
    (1) nums[n >> 1]
    (2) n & 1
         
    """
    nums = [0]
    for i in range(1, n+1):
        nums.append(nums[i >> 1] + (i & 1))  # note
    return nums
    
print(countBits(9))

# Note:
# nums.append(num[i&(i-1)] + 1)
# removes lowest set bit, and adds 1 for 1
# list will already contain counts for values < i
# also nums[i >> 1] == nums[i//2]