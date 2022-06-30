#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        queue = collections.deque()
        queue.append((root, 1))

        while queue:
            node, layer = queue.popleft()
            if node is None:
                continue
            if layer != len(res)+1:
                res.append(last_node.val)
            last_node = node
            queue.append((node.left, layer+1))
            queue.append((node.right, layer+1))
        res.append(last_node.val)
        return res
        
# @lc code=end

