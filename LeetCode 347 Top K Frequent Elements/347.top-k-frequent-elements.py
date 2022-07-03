#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        c = c.most_common(k) 
        return [c[i][0] for i in range(k)]

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        dic = collections.defaultdict(int)
        for item in nums:
            dic[item] += 1
        sort = sorted(dic.items(), key =lambda x:x[1], reverse=True)
        return [sort[i][0] for i in range(k)]
        
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        res = []
        dic = collections.defaultdict(int)
        for item in nums:
            dic[item] += 1
        return [heapq.nlargest(k, dic.items(), key=lambda x:x[1])[i][0] for i in range(k)]
# @lc code=end

