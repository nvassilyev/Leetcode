# https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    l, r = 0, len(height) - 1
    max_area = 0
    while l < r:
        max_area = max(max_area, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area