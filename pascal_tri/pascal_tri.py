"""
Runtime 41ms -> Beats 52.09% of users with Python3
Memory 15.94MB -> Beats 99.94% of users with Python3
"""
import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            sub = []
            for j in range(i+1):
                sub.append(math.comb(i, j))
            ans.append(sub)
        return ans
