#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    # 时间空间都是O(n)
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        cnt = 0
        dic = collections.defaultdict(int)
        for i in range(length):
            dic[nums[i]] += 1
            cnt += 1
            if cnt > k+1:
                dic[nums[i-k-1]] -= 1
                cnt -= 1
            if dic[nums[i]] > 1:
                return True
        return False
# @lc code=end
