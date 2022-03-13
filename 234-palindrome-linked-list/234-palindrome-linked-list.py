# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        s = ""
        curr = head
        
        while curr != None:
            s+= str(curr.val)
            curr = curr.next
        if s == "".join(reversed(s)):
            return True
        return False
        
        """
        :type head: ListNode
        :rtype: bool
        """
        