#O(nlogn) time
#O(1) space
class Solution:

    def findDuplicates(self, A):

        A.sort()

        for currIndex in range(len(A)-1):
            if A[currIndex] == A[currIndex+1]:
                return A[currIndex]

        return None

#O(n) time
#O(n) space
class Solution:

    def findDuplicates(self, A):
        arrDict = {}

        for i in A:
            if arrDict.get(i):
                return i
            arrDict[i] = True

        return None

sol = Solution()
A = [7,5,2,3,0,2,1]
output = sol.findDuplicates(A)
print(output)
