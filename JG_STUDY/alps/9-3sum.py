# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        size = len(nums)
        nums.sort()

        for idx in range(size - 2):
            left, right = idx + 1, size - 1

            if 0 < nums[idx]:
                continue

            while left < right:
                temp = nums[idx] + nums[left] + nums[right]
                if temp < 0:
                    left += 1
                elif 0 < temp:
                    right -= 1
                else:
                    temp_list = sorted([nums[idx], nums[left], nums[right]])
                    if temp_list not in result:
                        result.append(temp_list)
                    left += 1
                    right -= 1

        return result