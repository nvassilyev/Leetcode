# https://leetcode.com/problems/reverse-bits/

# @param n, an integer
# @return an integer

def reverseBits(n):
    reverse = 0
    for i in range(32):
        if (1 << (31 - i)) & n > 0:
            reverse |= (1 << i)
        else:
            reverse &= ~(1 << i)
    return reverse