# https://leetcode.com/problems/linked-list-cycle/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """

    # Tortoise and hare problem
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False