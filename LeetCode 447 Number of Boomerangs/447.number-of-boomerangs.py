#
# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#

# @lc code=start
class Solution:

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(pt1, pt2):
            return ((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)

        cnt = 0
        for pt_i in points:
            dis = collections.defaultdict(int)
            for pt_j in points:
                if pt_i == pt_j:
                    continue
                dis[distance(pt_i, pt_j)] += 1
            for v in dis.values():
                cnt += v * (v-1)
        return cnt
# @lc code=end

