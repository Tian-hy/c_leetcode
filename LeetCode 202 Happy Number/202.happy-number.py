#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def get_sum_of_square(self, num):
        sum = 0
        while num/10 >= 1:
            rem = num % 10
            num = int(num / 10)
            sum += rem**2
        sum += num**2
        return sum

    def isHappy(self, n: int) -> bool:
        res_sum = []
        sum = n
        while sum not in res_sum:
            if sum == 1:
                break
            print(res_sum)
            res_sum.append(sum)
            sum = self.get_sum_of_square(sum)
        
        if sum != 1:
            return False
        else:
            return True
        
        
# @lc code=end

