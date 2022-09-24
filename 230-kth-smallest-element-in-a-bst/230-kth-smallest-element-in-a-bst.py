# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        stack = [root]
        
        while stack:
            value = stack.pop()
            if value != None:
                nums.append(value.val)
                stack.append(value.left)
                stack.append(value.right)
        
        nums.sort()
        return nums[k-1]