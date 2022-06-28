# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head == None:
            return False
        
        cur = head
        lst = set()
        
        while cur:
            if cur in lst:
                return True
            lst.add(cur)
            cur = cur.next
        return False
            
        
        """
        :type head: ListNode
        :rtype: bool
        """
        