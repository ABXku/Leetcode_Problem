"""
Runtime = 44ms Beats 88.64% of users with Python3
Memory = 16.10MB Beats 99.30% of users with Python3
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        sum = 0
        for i, letter in enumerate(s):
            if (i + 1 != len(s))  and (dict[letter] < dict[s[i + 1]]):
                sum -= dict[letter]
            else: 
                sum += dict[letter]
        return sum