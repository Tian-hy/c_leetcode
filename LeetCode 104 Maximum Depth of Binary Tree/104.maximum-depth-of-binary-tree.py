#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)
        return max(left_max_depth, right_max_depth)+1


    def getDepth(self, node, parent_layer):
        if node is None:
            return
        if parent_layer+1 > self.layer:
            self.layer = parent_layer + 1
        self.getDepth(node.left, parent_layer+1)
        self.getDepth(node.right, parent_layer+1)

    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.layer = 0
        parent_layer = 0
        self.getDepth(root, parent_layer)
        return self.layer

        
# @lc code=end

