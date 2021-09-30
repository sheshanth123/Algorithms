class Solution:
    def solve(self, A):
        sum = 0
        arrayDict = {}

        for elemIndex in range(len(A)):
            sum += A[elemIndex]
            if sum==0:
                return [0, elemIndex]
            elif arrayDict.get(sum):
                return [elemIndex+1, arrayDict[sum]]
            arrayDict[sum]=elemIndex

sol = Solution()
A = [-1, 2, 1, -4, 2, 3,-1, 2]
output = sol.solve(A)
print(output)
