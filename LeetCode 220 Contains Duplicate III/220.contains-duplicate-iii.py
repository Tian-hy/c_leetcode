#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution:
    # O(n)
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket_width = t+1
        dic = {}

        for i, item in enumerate(nums):
            tmp = item//bucket_width
            if tmp in dic:
                return True
            if tmp-1 in dic and abs(dic[tmp-1] - item) <= t:
                return True
            if tmp+1 in dic and abs(dic[tmp+1] - item) <= t:
                return True
            
            dic[tmp] = item
            if i-k >= 0:
                del dic[nums[i-k]//bucket_width]
        return False

    # 没通过，超时
    def containsNearbyAlmostDuplicate1(self, nums: List[int], k: int, t: int) -> bool:
        cnt = 0
        win = collections.deque()
        for item in nums:
            if cnt >= k+1:
                win.popleft()
                cnt -= 1
            
            if len(win) > 0:
                lower = item - t
                upper = item + t
                for tmp in win:
                    if lower <= tmp and tmp <= upper:
                        return True
            win.append(item)
            cnt += 1
        return False
        
# @lc code=end

