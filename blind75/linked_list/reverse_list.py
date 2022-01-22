# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    # if not head:
    #     return None
    
    # cur = head.next
    # reverse = ListNode(head.val)
    
    # while cur:
    #     temp = reverse
    #     new = ListNode(cur.val)
    #     new.next = temp
    #     reverse = new
        
    #     cur = cur.next

    # return reverse

    prev = None
    cur = head

    while cur:
        n = cur.next
        cur.next = prev
        prev = cur
        cur = n

    return prev
    
    """
    Iter thru linked list
    store prev node (initally None) (n)
    make copy of cur.next
    cur.next will point to prev
    make cur now the next n
    """
    