#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        min_left_depth = self.minDepth(root.left)
        min_right_depth = self.minDepth(root.right)
        if None in [root.left, root.right]:
            return max(min_left_depth, min_right_depth)+1
        else:
            return min(min_left_depth, min_right_depth)+1
# @lc code=end

