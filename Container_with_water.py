# https://leetcode.com/problems/container-with-most-water/

def maxAreaBruteForce(height):
    """
    :type height: List[int]
    :rtype: int
    """
    area = 0
    for i in range(len(height)):
        j = i
        while j < len(height):
            curr = min(height[i], height[j]) * (j - i)
            if curr > area:
                area = curr
            j+=1
    return area

def maxArea(height):
    i, j = 0, len(height)-1
    water = 0
    while i < j:
        water = max(water, min(height[i], height[j]) * (j-i))
        if height[i] > height[j]:
            i += 1
        else:
            j += 1
    return water
    

print(maxArea([1,8,6,2,5,4,8,3,7]))