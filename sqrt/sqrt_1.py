"""
Runtime = 444ms -> Beats 23.64%of users with Python3
Memory = 16.10MB -> Beats 82.68%of users with Python3
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        x_half = int(x / 2)
        while((x_half * x_half) > x): 
            x_half = int(x_half / 2)
        while(x_half * x_half < x):
            x_half = x_half + 1
        if (x_half * x_half) == x:
            return x_half
        else:
            return (x_half - 1)
            
            
            
solution = Solution()
print(solution.mySqrt(9))