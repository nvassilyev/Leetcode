# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s: str) -> int:
    """
    :type s: str
    :rtype: int
    """
    
    longest = ""
    curr = ""
    i = 0
    index = 1
    
    while i != len(s):
        
        if s[i] not in curr:
            curr += s[i]
        else:
            curr = s[index]
            i = index
            index += 1
            
        if len(curr) > len(longest):
            longest = curr
            
        i += 1
    
    return len(longest)

print(lengthOfLongestSubstring("abcdeagh")) 

# Elegant solution:

# used = {}
#     max_length = start = 0
#     for i, c in enumerate(s):
#         if c in used and start <= used[c]:
#             start = used[c] + 1
#         else:
#             max_length = max(max_length, i - start + 1)
            
#         used[c] = i

#     return max_length
            
            