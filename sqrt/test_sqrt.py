# If you want to test with sqrt_2.py, just change sqrt_1 to sqrt_2
from sqrt_1 import Solution
import pytest

solution = Solution()
def test_sqrt():
    assert solution.mySqrt(0) == 0
    assert solution.mySqrt(1) == 1
    assert solution.mySqrt(2) == 1
    assert solution.mySqrt(8) == 2
    assert solution.mySqrt(9) == 3
    assert solution.mySqrt(10) == 3