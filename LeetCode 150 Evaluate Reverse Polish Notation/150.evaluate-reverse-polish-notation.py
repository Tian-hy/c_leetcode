#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(left+right)
            elif item == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left-right)
            elif item == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(left*right)
            elif item == "/":
                right = stack.pop()
                left = stack.pop()
                tmp =  left / right
                if tmp > 0:
                    tmp = left // right
                else:
                    tmp = math.ceil(left / right)
                stack.append(tmp)
            else:
                stack.append(int(item))
        return stack.pop()
# @lc code=end

