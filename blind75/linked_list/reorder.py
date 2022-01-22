#  https://leetcode.com/problems/reorder-list/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    
    # O(n^2) solution 
    # ptr = head
    # cur = None
    
    # if not head.next or not head.next.next:
    #     return
    
    # while not (cur == ptr or cur == ptr.next):
    #     cur = ptr
    #     while cur.next.next:
    #         cur = cur.next
    #     last = cur.next
    #     cur.next = None
        
    #     last.next = ptr.next
    #     ptr.next = last
    #     ptr = ptr.next.next
    
    # Base Case
    if not head.next:
        return
    
    # Find mid point
    mid = fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        mid = mid.next
    
    # Reverse second half of list
    r = ListNode(mid.next.val)
    r.next = None
    cur = mid.next.next
    while cur:
        new = ListNode(cur.val)
        new.next = r
        r = new
        cur = cur.next
    
    # Merge two lists
    cur = head
    mid.next = None  #Chop second half of original list (we don't need it)
    while cur and r:
        p1 = cur.next
        p2 = r.next
        r.next = p1
        cur.next = r
        cur = p1
        r = p2