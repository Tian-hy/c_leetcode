#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def getLine(x1, y1, x2, y2):
            if x1 == x2:
                return 0, 0, x1
            k = (y2-y1)/(x2-x1)
            b = y1-k*x1
            return k, b, 0
        
        if len(points) == 1:
            return 1

        dic = collections.defaultdict(set)
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                k, b, x = getLine(x1, y1, x2, y2)
                dic[str([k, b, x])].add((x1, y1))
                dic[str([k, b, x])].add((x2, y2))
        cnt = [len(item) for item in dic.values()]
        return max(cnt)
# @lc code=end

