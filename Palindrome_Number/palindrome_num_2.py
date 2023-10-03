"""
Runtime 68ms -> Beats 28.49% of users with Python3
Memory 16.23MB -> Beats 59.72% of users with Python3
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            x_rev = 0
            x_temp =  x
            while (x_temp != 0):
                digit = x_temp % 10
                x_rev = (x_rev * 10) + digit
                x_temp = int(x_temp / 10)
            if x == x_rev:
                return  True
            else:
                return False
        else:
            return False