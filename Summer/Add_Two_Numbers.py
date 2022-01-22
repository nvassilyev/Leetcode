# Definition for singly-linked list.
# https://leetcode.com/problems/add-two-numbers/
# from typing import List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1 = 0
        curr = l1
        while (curr):
            curr = curr.next
            len1 += 1

        len2 = 0
        curr2 = l2
        while (curr2):
            curr2 = curr2.next
            len2 += 1
        
        flag = True
        if len1 < len2:
            flag = False 

        sum = 0
        for i in range(max(len1, len2)):
            if i >= min(len1, len2):
                if flag:
                    sum += l1.val * 10**i
                    l1 = l1.next
                else:
                    sum += l2.val * 10**i
                    l2 = l2.next
            else:
                sum += (l1.val * 10**i) + (l2.val * 10**i)
                l1 = l1.next
                l2 = l2.next
                
        digits = [int(x) for x in str(sum)]
        
        solution = ListNode()
        curr = solution
        for i, digit in enumerate(reversed(digits)):
            curr.val = digit
            if i != len(digits) - 1:
                curr.next = ListNode()
                curr = curr.next
        return solution    
        

       
        

    