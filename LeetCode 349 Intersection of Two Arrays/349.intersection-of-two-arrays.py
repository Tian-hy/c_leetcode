#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        res = []
        for item in nums1:
           dic[item] = 1
        for item in nums2:
            if item in dic.keys():
                if item not in res:
                    res.append(item)
        return res
# @lc code=end

