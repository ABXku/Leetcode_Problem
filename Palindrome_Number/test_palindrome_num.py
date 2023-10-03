# If you want to test with palindrome_num_2.py, just change palindrome_num_1 to palindrome_num_2
from palindrome_num_1 import Solution

solution = Solution()
def test_palindrome_num():
    assert solution.isPalindrome(121) == True
    assert solution.isPalindrome(0) == True
    assert solution.isPalindrome(11) == True
    assert solution.isPalindrome(100) == False
    assert solution.isPalindrome(-121) == False
    assert solution.isPalindrome(10) == False