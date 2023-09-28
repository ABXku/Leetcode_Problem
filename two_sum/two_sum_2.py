"""
    Runtime = 587ms -> Beats 38.18% of users with Python3
    Memory = 17.40MB -> Beats 57.21%of users with Python3
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index = {}
        for i in range(len(nums)):
            index[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i]) in nums and index[target - nums[i]] != i:
                return [i, index[target - nums[i]]]