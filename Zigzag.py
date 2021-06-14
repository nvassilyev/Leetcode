# https://leetcode.com/problems/zigzag-conversion/

# PAYPALISHIRING
"""
PAY P ALI S HIR I NG

0 1 2 3 4 5 6 

P   A   H   N   0
A P L S I I G   1
Y   I   R       2

P     I     N   0
A   L S   I G   1
Y A   H R       2
P     I         3

x , y
go down x + numrows
go diagonal (x - 1, y + 1) * numrows - 1

"""

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """

    i = x = y = k = 0
    j = 1
    down = True
    
    solution = [[0 for j in range(len(s))] for i in range(numRows)]

    while i < len(s):
        print(down)
        print(x, y)
        print(j, k)
        solution[x][y] = s[i]  
        
        if j == numRows:
            down = False
            j = 0
        if k == numRows - 1:
            down = True
            k = 0
        
        if down:
            j += 1
            x += 1
        else:
            k += 1
            x -= 1
            y += 1
        
        i += 1
        
    print(solution)

convert("PAYPALISHIRING", 4)
            
