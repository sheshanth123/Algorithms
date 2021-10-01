# time -> O(logn)
# space - > O(1)

class Solution:
    def solve(self, A, target):
        mid = 0
        start = 0
        end = len(A)

        while(start <= end):
            mid = (start + (end-start))//2

            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return -1

sol = Solution()
A = [1,2,3,4,5]
target = 3
output = sol.solve(A, target)
print(output)
