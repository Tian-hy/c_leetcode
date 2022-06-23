#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = collections.defaultdict(list)
        for item in strs:
            tmp = str(sorted([ch for ch in item]))
            anagram[tmp].append(item)
        return list(anagram.values())
# @lc code=end

