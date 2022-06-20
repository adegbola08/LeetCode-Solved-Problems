# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        cur = head
        lst = []
        
        while cur != None:
            if cur.next in lst:
                return True
            lst.append(cur.next)
            cur = cur.next
        return False
            
        
        """
        :type head: ListNode
        :rtype: bool
        """
        