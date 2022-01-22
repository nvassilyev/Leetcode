# https://leetcode.com/problems/climbing-stairs/

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    # too slow but works
    # def backtrack(curr):
    #     if curr == n:
    #         return 1
    #     else:
    #         total = 0
    #         total += backtrack(curr+1)
    #         if n - curr > 1:
    #             total += backtrack(curr+2)
    #         return total
        
    # return backtrack(0)
    
    total = [1, 2]
        
    for i in range(2, n):
        total.append(total[i-1] + total[i-2])
    return total[n-1]
            
    # Notice pattern: getting to step i is number of times it took
    # to get to step i-1 and i-2
    # 1: 1 (1)
    # 2: 1,1 - 2 (2)
    # 3: 1,1,1 - 1,2 - 2,1 (3)
    # 4: 1,1,1,1 - 1,1,2 - 1,2,1 - 2,1,1 - 2,2 (5)

print(climbStairs(45))