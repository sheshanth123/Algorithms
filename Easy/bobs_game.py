# Bob is playing a game with himself. He gives himself a list nums. Each round, Bob chooses two elements of the list and replaces them with one positive integer with the same sum as the numbers he selected. Bob declares victory when all of the number in the array are even.

# Return the minimum number of rounds Bob must make before he can declare victory, or return -1 if Bob can never declare victory.

# Constraints

# 2 ≤ N ≤ 100,000 where N is the length of nums.
# 0 ≤ nums[i] ≤ 100,000
# Example 1
# Input

# nums = [1, 1, 3, 7, 6, 12]
# Output

# 2
# Explanation

# Bob can take:

# 1 and 1 to make 2.
# 3 and 7 to make 10.
# In the end we have [2, 10, 18]

# Example 2
# Input

# nums = [0, 2, 2, 3, 5, 7]
# Output

# -1
# Explanation

# Whether we merge 3 and 5, 3 and 7, or 5 and 7, we are left with one odd integer. The odd integer can't merge with any even integer to become even.
class Solution:
    def solve(self, nums):
        odd_nums = sum([1 for i in nums if i%2!=0 ])
        if odd_nums%2 == 0: return odd_nums//2 
        else: return -1
# Solution
# We count the number of odd numbers in the list. If we sum two odd numbers together, the result will be even - so the optimal number of moves if the number of odds is divisible by two.

# If there is an odd number of odd numbers - we get stuck with one odd number at the end we can't get rid of.
