# time -> O(n) 
# space -> O(1)

class Solution:
    def solve(self, A):
        maxSum = A[0]
        maxEndingHere = A[0]

        #using kadane's algorithm

        for elemIndex in range(1, len(A)-1):
            maxEndingHere = max(A[elemIndex], A[elemIndex]+maxEndingHere)
            maxSum = max(maxSum, maxEndingHere)

        return maxSum

sol = Solution()
A = [2, -3,4,-1,-2,1,5,-1]
output = sol.solve(A)
print(output)
