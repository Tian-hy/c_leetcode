#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    class Command:
        def __init__(self, com, node):
            self.com, self.node = com, node

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        que = collections.deque()
        que.append((self.Command('go', root), 1))
        last_layer = 1
        tmp_list = []

        while que:
            tmp, i = que.popleft()
            if tmp.node is None:
                continue

            if tmp.com == 'go':
                que.append((self.Command('print', tmp.node), i))
                que.append((self.Command('go', tmp.node.left), i+1))
                que.append((self.Command('go', tmp.node.right), i+1))
            elif tmp.com == 'print':
                if i == last_layer:
                    tmp_list.append(tmp.node.val)
                else:
                    res.append(tmp_list)
                    tmp_list = [tmp.node.val]
                    last_layer = i
        res.append(tmp_list)
        return res

# @lc code=end

