# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        result = 0
        stack = []
        if root:
            stack.append((root, 1))
        
        while stack:
            cur, level = stack.pop()
            result = max(result, level)
            if cur.left:
                stack.append((cur.left, level+1))
            if cur.right:
                stack.append((cur.right, level+1))
        
        return result


        