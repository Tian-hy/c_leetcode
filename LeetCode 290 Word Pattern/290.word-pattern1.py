#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = pattern
        s = s.split()
        return list(map(t.find, t)) == list(map(s.index, s))
# @lc code=end

