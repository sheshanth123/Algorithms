# time O(n)
# space O(n)
class Solution:

    def fibonacci(self, A, mapVal):
        if A==1 or A==2:
            return 1
        elif mapVal.get(A):
            return mapVal.get(A)
        result = self.fibonacci(A-1, mapVal) + self.fibonacci(A-2, mapVal)
        mapVal[A] = result
        return result

    def solve(self, A):
        return self.fibonacci(A, {})
                 
sol = Solution()
A = 5
output = sol.solve(A)
print(output)
