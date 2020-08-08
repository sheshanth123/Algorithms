# Given a list of positive integers nums, return the number of integers that have odd number of digits.

# Example 1
# Input

# nums = [1, 800, 2, 10, 3]
# Output

# 4
# Explanation

# [1, 800, 2, 3] have odd number of digits.

class Solution:
    def solve(self, nums):
        return sum([1 for i in nums if len(str(i)) % 2 != 0])

# I think len is faster than sum in python and since we can solve it with len,
# find the length of a list which you generated for odd strings

# Time complexity: O(n)
