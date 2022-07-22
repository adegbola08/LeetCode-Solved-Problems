# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new = head
        count = 0
        while new:
            new = new.next
            count += 1
        
        
        dummy = ListNode()
        cur = dummy
        
        while head:
            if count == n:
                cur.next = head.next
                break
            temp = head.next
            head.next = None
            cur.next = head
            head = temp
            cur = cur.next
            count -= 1
            
        return dummy.next
        