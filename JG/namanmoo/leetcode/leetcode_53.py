# https://leetcode.com/problems/maximum-subarray/
# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = answer = nums[0]

        for i in range(1, len(nums)):
            if 0 < answer:
                answer += nums[i]
            else:
                answer = nums[i]

            max_value = max(answer, max_value)

        return max_value
