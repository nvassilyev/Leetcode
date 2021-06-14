def reverse1(x):
    reverse = 0
    negative = x < 0
    if x < 0:
        x *= -1
        
    while x != 0:
        if reverse > (10000 - (x % 10)) // 10:
            return 0
        reverse = (reverse * 10) + (x % 10)
        x //= 10
        
    return -reverse if negative else reverse

print(reverse1(-1000))