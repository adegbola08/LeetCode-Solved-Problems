# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0
        
        while stack:
            value, depth = stack.pop(0)
            
            if value:
                res = max(res, depth)
                stack.append([value.left, depth+1])
                stack.append([value.right, depth+1])
                
        return res
                
                
        