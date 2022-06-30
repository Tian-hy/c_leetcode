#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    '''
    s = ['(', '[', ']', ')']
    stack = []
    stack = ['('], item = (
    stack = ['(', '['], item = [
    stack = ['('], item = ]
    stack = [], item = )
    return True
    '''
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', ']': '[', '}': '{'}
        ss = set((')', ']', '}'))
        for item in s:
            if item not in ss:
                stack.append(item)
            else:
                if len(stack):
                    tmp = stack.pop()
                else:
                    return False
                if tmp != dic[item]:
                    return False
        if len(stack):
            return False
        return True
        
# @lc code=end

