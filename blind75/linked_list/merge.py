#  https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(ist1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    merge = None
    while list1 or list2:
        if not list1 or (list2 and list1.val > list2.val):
            n = ListNode(list2.val)
            list2 = list2.next
        else:
            n = ListNode(list1.val)
            list1 = list1.next
            
        if not merge:
            merge = cur = n
        else:
            cur.next = n
            cur = cur.next
        
    return merge

    # Recursive
    # if not list1:
    #     return list2
    # if not list2:
    #     return list1
    # if list1.val < list2.val:
    #     list1.next = mergeTwoLists(list1.next, list2)
    #     return list1
    # else:
    #     list2.next = mergeTwoLists(list1, list2.next)
    #     return list2