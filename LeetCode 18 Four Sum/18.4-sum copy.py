#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNSum(nums, target, N, result, results):
            if len(nums)<N or N<2 or target < N*nums[0] or target > N*nums[-1]:
                return
            if N == 2:
                l, r = 0, len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        results.append(result + [nums[l], nums[r]])
                        print(results)
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                        findNSum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        results = []
        nums.sort()
        findNSum(nums, target, 4, [], results)
        return results
# @lc code=end