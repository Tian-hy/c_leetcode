#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from calendar import isleap


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            if abs(left-right) <= 1 and left != -1 and right != -1:
                return max(left, right) + 1
            else:
                return -1
        return check(root) != -1
        
    def isBalanced1(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        is_left_bal = self.isBalanced(root.left)
        is_right_bal = self.isBalanced(root.right)
        if abs(left_depth - right_depth) <= 1 and is_left_bal and is_right_bal:
            return True
        else:
            return False

    def getDepth(self, root):
        if not root:
            return 0
        return max(self.getDepth(root.right), self.getDepth(root.left))+1
        
# @lc code=end

