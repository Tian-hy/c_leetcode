#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = collections.deque()
        queue.append((root, 1))
        res, tmp = [], []

        while queue:
            node, layer = queue.popleft()
            if node is None:
                continue
            if layer == len(res)+1:
                tmp.append(node.val)
            else:
                res.append(tmp)
                tmp = [node.val]
            queue.append((node.left, layer+1))
            queue.append((node.right, layer+1))
        res.append(tmp)
       
        for i in range(len(res)//2):
            res[-1-i], res[i] = res[i], res[-1-i]
        
        return res



# @lc code=end

