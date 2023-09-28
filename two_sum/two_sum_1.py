"""
    Runtime = 2489ms -> Beats 26.86% of users with Python3
    Memory = 16.93MB -> Beats 98.08% of users with Python3
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
