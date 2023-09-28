"""
Runtime = 44ms -> Beats 59.60% of users with Python3
Memory = 16.18MB -> Beats 82.15% of users with Python3
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        while low <= high:
            mid = low + int((high - low)/2)
            if mid == x / mid:
                return mid
            elif mid > x / mid:
                high = mid - 1
            elif mid < x / mid:
                low = mid + 1
        return high