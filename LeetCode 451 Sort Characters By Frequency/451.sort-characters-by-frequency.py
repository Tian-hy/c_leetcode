#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        res = ""
        freq = collections.defaultdict(int)
        for item in s:
            freq[item] += 1

        freq = sorted(freq.items(), key = lambda x:x[1], reverse = True)
        for item in freq:
            res += item[0]*item[1]
        return res
# @lc code=end

