#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        queue = collections.deque()
        queue.append((n, 0))
        visited = set()
        visited.add(n)

        while queue:
            num, step = queue.popleft()

            if num == 0:
                return step
            
            i = 1
            while num - i**2 >= 0:
                n = num - i**2
                if n == 0:
                    return step + 1
                i += 1
                if n in visited:
                    continue
                visited.add(n)
                queue.append((n, step+1))
# @lc code=end

