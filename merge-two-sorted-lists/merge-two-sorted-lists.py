# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        while l1 or l2:
            val1 = l1.val if l1 or l1 == 0 else None
            val2 = l2.val if l2 or l2 == 0 else None
            
            if (val1 or val1 == 0) and (val2 or val2 == 0):
                if val1 <= val2:
                    temp = l1.next
                    l1.next = None
                    cur.next = l1
                    l1 = temp
                else:
                    temp = l2.next
                    l2.next = None
                    cur.next = l2
                    l2 = temp
            elif val1 or val1 == 0:
                cur.next = l1
                break
            else:
                cur.next = l2
                break
            cur = cur.next
            
        return dummy.next
                    
        
        