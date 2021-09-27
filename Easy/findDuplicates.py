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
