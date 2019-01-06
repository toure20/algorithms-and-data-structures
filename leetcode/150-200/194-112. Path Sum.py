# 112. Path Sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.curSum = 0
        def dfs(node):
            if not node: return False
            self.curSum += node.val
            if not node.left and not node.right and self.curSum == sum:
                return True
            flag = dfs(node.left) or dfs(node.right)
            self.curSum -= node.val
            return flag
                 
        return dfs(root)
        