"""
You are given an array of integers and a pivot. Rearrange the array in the
following order:
[all elements less than pivot, elements equal to pivot, elements greater than pivot]

For example,
a = [5,2,4,4,6,4,4,3] and pivot = 4 --> result = [3,2,4,4,4,4,5,6].
"""
# time O(n)
# space O(1)

class Solution:

    def swap(self, inpA, inpB):
        return inpB, inpA

    def solve(self, A, pivot):
        lenA = len(A)
        boundryLeft = 0
        boundryRight = lenA-1

        elemIndex = 0

        while(elemIndex<=boundryRight):
            if A[elemIndex] < pivot:
                A[elemIndex], A[boundryLeft] = self.swap(A[elemIndex], A[boundryLeft])
                boundryLeft += 1
                elemIndex+=1

            elif A[elemIndex] > pivot:
                A[elemIndex], A[boundryRight] = self.swap(A[elemIndex], A[boundryRight])
                boundryRight -= 1
            else:
                elemIndex +=1
        return A

sol = Solution()
A = [3,2,1,4,3,6,7,5]
pivot = 4
output = sol.solve(A, pivot)
print(output)
