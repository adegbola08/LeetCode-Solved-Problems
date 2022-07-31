# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        count = 0
        cur = head
        
        while cur:
            count += 1
            cur = cur.next
        
        times = k % count
        
        temp = ListNode()
        tempHead = temp
        
        cur2 = head
        
        while cur2:
            count -= 1
            if count == times:
                tempHead.next = cur2.next
                cur2.next = None
            cur2 = cur2.next
        
        while tempHead:
            if tempHead.next == None:
                tempHead.next = head
                break
            tempHead = tempHead.next
      
        return temp.next
        
                
            
        