#using recursion
class Solution:
  def solve(self, A):
    if A==1 or A==2:
      return 1
    return self.solve(A-1) + self.solve(A-2)

#using for loop
class Solution:

    def solve(self, A):
        n1=1
        n2=1
        fibSum = 0

        for nVal in range(2,5):
            fibSum=n1+n2
            n2=n1
            n1=fibSum
        return fibSum
        
            
sol = Solution()
A = 5
output = sol.solve(A)
print(output)
