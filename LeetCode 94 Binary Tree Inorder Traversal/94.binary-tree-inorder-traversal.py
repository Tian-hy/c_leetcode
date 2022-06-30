#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 非递归
    class Command:
        def __init__(self, com, node):
            self.com, self.node = com, node

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [self.Command('go', root)]
        while stack:
            tmp = stack.pop()
            if tmp.node is None:
                continue
            if tmp.com == 'go':
                stack.append(self.Command('go', tmp.node.right))
                stack.append(self.Command('print', tmp.node))
                stack.append(self.Command('go', tmp.node.left))
            elif tmp.com == 'print':
                res.append(tmp.node.val)
        return res

    # 递归
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.res.append(root.val)
            self.inorder(root.right)

    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.inorder(root)
        return self.res
        
# @lc code=end

