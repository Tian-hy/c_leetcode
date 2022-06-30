#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 用栈模拟递归做
    class Command:
        def __init__(self, com, node):
            self.com, self.node = com, node

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [self.Command('go', root)]
        while stack:
            tmp = stack.pop()
            if tmp.node is None:
                continue
            if tmp.com == 'go':
                stack.append(self.Command('go', tmp.node.right))
                stack.append(self.Command('go', tmp.node.left))
                stack.append(self.Command('print', tmp.node))
            elif tmp.com == 'print':
                res.append(tmp.node.val)
        return res
        

    # 递归做
    def preorder(self, root):
        if root is None:
            return
        self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def preorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.preorder(root)
        return self.res
    
    # 这个也不错
    def preorderTraversal2(self, root): 
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret
# @lc code=end

