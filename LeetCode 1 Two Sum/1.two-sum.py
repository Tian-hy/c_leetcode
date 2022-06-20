#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    # 有两种思路，第一种是先排序后用对撞指针
    #           第二种是用查找表，对每个元素a，查找target-a是否存在
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try:
                j = nums[i+1:].index(target - nums[i])
                return [i, i+j+1]
            except:
                pass

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            remaining = target - val
            if remaining in seen.keys():
                return [seen[remaining], i]
            else:
                seen[val] = i

        
# @lc code=end

