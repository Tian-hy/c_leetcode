#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getDepth(root):
            if not root:
                return 0
            return getDepth(root.left)+1

        if not root:
            return 0
        left_depth = getDepth(root.left)
        right_depth = getDepth(root.right)
        if left_depth == right_depth:
            return pow(2, left_depth) + self.countNodes(root.right)
        else:
            return self.countNodes(root.left) + pow(2, right_depth)

    def countNodes1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left+right+1
        
        
# @lc code=end

