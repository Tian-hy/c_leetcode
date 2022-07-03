#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSym(self, l, r):
        if not l and not r:
            return True
        
        if not l or not r:
            return False

        if l.val != r.val:
            return False

        res1 = self.isSym(l.left, r.right)
        res2 = self.isSym(l.right, r.left)
        if res1 and res2:
            return True
        else:
            return False
            

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l = root.left
        r = root.right
        return self.isSym(l, r)
# @lc code=end

