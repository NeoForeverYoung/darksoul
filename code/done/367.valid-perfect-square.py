#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num+1
        while left < right:
            mid = (left+right)//2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid
            else:
                left = mid+1
        return False

# @lc code=end
