#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
import enum


class Solution:
    # 时间和空间复杂度都是O(n^2)
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = 0
        search3_and_4 = collections.defaultdict(int)
        for v3 in nums3:
            for v4 in nums4:
                s = v3+v4
                search3_and_4[s] += 1
        
        for vali in nums1:
            for valj in nums2:
                s = vali + valj
                target = 0 - s 
                if target in search3_and_4:
                    cnt += search3_and_4[target]
        
        return cnt
        
# @lc code=end

