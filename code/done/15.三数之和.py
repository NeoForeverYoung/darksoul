#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n - 1
            x = nums[i]
            if x + nums[j] + nums[j+1] > 0:
                break
            if x + nums[k] + nums[k-1] < 0:
                continue
            while j < k:
                s = x + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j+=1
                    while j< k and nums[j] == nums[j-1]:
                        j+=1
                    k-=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
        return ans
                    

# @lc code=end

