class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        """
        S(n-1) = F(n+1) – F(1) 
        S(n-1) = F(n+1) – 1 
        S(n) = F(n+2) – 1 —-(1)
        In order to find S(n), simply calculate the (n+2)’th Fibonacci number and subtract 1 from the result.
        """
        return self.findNthFib(A+2) - 1
        

    def findNthFib(self, inpInt):
        if inpInt == 1:
            return 1
        elif inpInt == 0:
            return 0
        return self.findNthFib(inpInt-1) + self.findNthFib(inpInt-2)

sol = Solution()

print(sol.solve(5))
