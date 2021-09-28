"""
O(n) time
O(1) space

"""
class Solution:

    def swap(self, inpA, inpB):
        inpA = inpA + inpB
        inpB = inpA - inpB
        inpA = inpA - inpB
        return inpA, inpB

    def traverse(self, A):
        
        lenA = len(A)
        
        for elemIndex in range(lenA//2):
            A[elemIndex], A[lenA-1-elemIndex] = self.swap(A[elemIndex], A[lenA-1-elemIndex])
        return A


sol = Solution()

A = [3,2,4,5,6,3]

output = sol.traverse(A)
print(output)
