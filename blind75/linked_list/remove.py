# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    
    slow = head
    cur = head
    i = 1
    
    while cur.next:
        if i > n:
            slow = slow.next
        i += 1
        cur = cur.next
    if i <= n:
        return head.next
    if slow.next.next:
        slow.next = slow.next.next
    else:
        slow.next = None
    return head