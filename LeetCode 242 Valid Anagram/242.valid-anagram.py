#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for item in s:
            dic[item] = 1 if item not in dic.keys() else dic[item]+1
        for item in t:
            if item in dic.keys() and dic[item] > 0:
                dic[item] -= 1
            else:
                return False
        
        # 要注意是否所有的values是不是都等于0，只有完全一样才行
        for v in dic.values():
            if v > 0:
                return False
        return True
# @lc code=end

