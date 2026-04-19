# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxDiff = 0
        def dfs(curr):
            if not curr:
                return 0
            lHeight = dfs(curr.left)
            rHeight = dfs(curr.right)
            self.maxDiff = max(self.maxDiff, abs(lHeight - rHeight))
            return max(lHeight, rHeight) + 1
        
        dfs(root)
        if self.maxDiff > 1:
            return False
        return True

