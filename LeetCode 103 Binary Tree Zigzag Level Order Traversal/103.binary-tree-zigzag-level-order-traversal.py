#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res, tmp = [], []
        queue = collections.deque()
        queue.append((root, 1))

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

        for i in range(len(res)):
            if i%2:
                for j in range(len(res[i])//2):
                    res[i][j], res[i][-1-j] = res[i][-1-j], res[i][j]
        return res
# @lc code=end

