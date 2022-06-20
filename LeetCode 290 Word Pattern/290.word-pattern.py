#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        s_split = s.split()
        target = ""
        print( pattern, s)
        for i in range(len(pattern)):
            if pattern[i] not in dic.keys():
                if i < len(s_split):
                    dic[pattern[i]] = s_split[i] if s_split[i] not in dic.values() else ""
                else:
                    dic[pattern[i]] = " "
            target += dic[pattern[i]]
        
        if target == s.replace(" ", ""):
            return True
        return False
# @lc code=end

