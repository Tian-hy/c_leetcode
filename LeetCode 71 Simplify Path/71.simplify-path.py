#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        tmp = ""
        for item in path:
            if item == '/':
                if len(tmp):
                    if tmp == ".":
                        pass
                    elif tmp == "..":
                        if len(stack):
                            stack.pop()
                    else:
                        stack.append(tmp)
                tmp = ""
            else:
                tmp += item
        # 最后一段tmp
        if len(tmp):
            if tmp == ".":
                pass
            elif tmp == "..":
                if len(stack):
                    stack.pop()
            else:
                stack.append(tmp)
        
        # 重构path
        path = ''
        for item in stack:
            path += '/'
            path += item
        if path == '':
            path = '/'
        return path
# @lc code=end

