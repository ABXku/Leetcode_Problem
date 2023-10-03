"""
Runtime 59ms -> Beats 64.82% of users with Python3
Memory 16.26MB -> Beats 59.72% of users with Python3
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0 and str(x) == str(x)[::-1]:
            return True
        else:
            return False