"""
move all zeros to begining of array
A = [2,5,-1,0,4,-2,0]
[0, 0, 2, 5, -1, 4, -2]
"""
# time O(n)
# space O(n)

class Solution:
    def solve(self, A):
        newArr = []

        for elem in A:
            if elem:
                continue
            newArr.append(elem)

        for elem in A:
            if elem:
                newArr.append(elem)

        return newArr

sol = Solution()
A = [2,5,-1,0,4,-2,0]
output = sol.solve(A)
print(output)
