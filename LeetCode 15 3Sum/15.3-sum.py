#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negi, pos, zero = [], [], []
        res = set()
        
        # 分成大于0，小于0和等于0
        for item in nums:
            if item > 0:
                pos.append(item)
            elif item == 0:
                zero.append(item)
            else:
                negi.append(item)
        pos_set = set(pos)
        negi_set = set(negi)

        # 如果=0的大于三个，res增加[0, 0, 0]
        if len(zero) >= 3:
            res.add((0, 0, 0))
        
        # 如果=0有1个或2个，需要判断neg=-1*pos
        if len(zero) > 0:
            for item in pos:
                if -1*item in negi_set:
                    res.add((-1*item, 0, item))

        # pos中有两个，neg中有一个
        for i, vali in enumerate(pos):
            for j, valj in enumerate(pos[i+1:]):
                remaining = -1*(vali+valj)
                if remaining in negi_set:
                    res.add((remaining, min(vali, valj), max(vali, valj)))

        # neg中有两个， pos中有一个
        for i, vali in enumerate(negi):
            for j, valj in enumerate(negi[i+1:]):
                remaining = -1*(vali+valj)
                if remaining in pos_set:
                    res.add((remaining, min(vali, valj), max(vali, valj)))
        return res

    def threeSum1(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

# @lc code=end
