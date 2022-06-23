#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
        return result

    def threeSumClosest1(self, nums: List[int], target: int) -> int:
        def findNCloset(nums, target, N, result):
            if len(nums) < N or N < 2:
                return
            if N == 2:
                l, r = 0, len(nums)-1
                while (l < r):
                    s = nums[l] + nums[r]
                    if abs(s-target) < self.closet:
                        self.closet = abs(s-target)
                        self.res = result + [nums[l], nums[r]]
                    if s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i>0 and nums[i] != nums[i-1]):
                        findNCloset(nums[i+1:], target-nums[i], N-1, result+[nums[i]])
        self.res = []
        nums.sort()
        self.closet = float("inf")
        findNCloset(nums, target, 3, [])
        return sum(self.res)
# @lc code=end

