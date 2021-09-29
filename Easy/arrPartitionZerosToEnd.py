"""
Given an array of integers, rearrange the elements such that all zeros are
moved to the end of the array.
time O(n)
space O(1)
"""

class Solution:
    def solve(self, A):
        boundry = len(A)-1

        for elemIndex in range(len(A)-1, -1, -1):
            if A[elemIndex] is 0:
                A[elemIndex] = A[boundry]
                A[boundry] = 0
                boundry -=1

        return A

sol = Solution()
A = [0, 0,0,2,5,-1,0,4,-2,0]
output = sol.solve(A)
print(output)
