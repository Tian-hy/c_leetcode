#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 用栈模拟递归
    class Command:
        def __init__(self, com, node):
            self.com = com
            self.node = node

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [self.Command('go', root)]
        while stack:
            tmp = stack.pop()

            if tmp.node is None:
                continue

            if tmp.com == 'go':
                stack.append(self.Command('print', tmp.node))
                stack.append(self.Command('go', tmp.node.right))
                stack.append(self.Command('go', tmp.node.left))
            elif tmp.com == 'print':
                res.append(tmp.node.val)
        return res

    # 用递归解
    def postorder(self, res, root):
        if root:
            self.postorder(res, root.left)
            self.postorder(res, root.right)
            res.append(root.val)

    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postorder(res, root)
        return res
    

        
# @lc code=end

