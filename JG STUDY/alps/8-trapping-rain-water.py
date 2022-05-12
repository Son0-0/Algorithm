# 171 ms 16.8 MB
# https://leetcode.com/problems/trapping-rain-water/
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4, 2, 0, 3, 2, 5]
# height = [4, 2, 3]

class Solution:
    def trap(self, height: List[int]) -> int:
        left_pointer, right_pointer = 0, 0
        list_size = len(height)

        result = 0
        bucket = []
        while left_pointer != list_size - 1:
            for h in range(left_pointer + 1, list_size):
                if height[left_pointer] <= height[h]:
                    while bucket:
                        result += bucket.pop()[1]
                    left_pointer = h
                    break
                else:
                    bucket.append((height[h], height[left_pointer] - height[h]))

            if bucket:

                bucket = list(reversed(bucket))
                bucket.append((height[left_pointer], height[left_pointer]))
                bucket = list(reversed(bucket))

                left_pointer += len(bucket) - 1

                cur_height = bucket.pop()[0]

                temp_w = 0
                while bucket:
                    comp_height = bucket.pop()[0]
                    if cur_height <= comp_height:
                        cur_height = comp_height
                    else:
                        temp_w += cur_height - comp_height

                result += temp_w

        return result