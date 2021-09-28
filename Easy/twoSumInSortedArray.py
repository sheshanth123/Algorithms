"""
Two sum in sorted array
A = [1,2,3,4,5,6]
target  = 9

time -> O(n)
space -> O(1)
"""

class Solution:

    def twoSum(self, A, target):

        lenA = len(A)
        start = 0
        end = lenA - 1

        while start < end:
            sum = A[start] + A[end]

            if sum == target:
                return [A[start], A[end]]
            elif sum > target:
                end -=1
            else:
                start +=1

        return []

sol = Solution()

A = [1,2,3,4,5,6]
target  = 9

output = sol.twoSum(A, target)
print(output)
