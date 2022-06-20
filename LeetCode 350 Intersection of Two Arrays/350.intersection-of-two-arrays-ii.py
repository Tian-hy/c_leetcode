#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        res = []
        for item in nums1:
            if item not in dic.keys():
                dic[item] = 1
            else:
                dic[item] += 1
        for item in nums2:
            if item in dic.keys():
                if dic[item] > 0:
                    res.append(item)
                    dic[item] -= 1
        return res


        
# @lc code=end

