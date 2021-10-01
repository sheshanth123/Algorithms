class Solution:
    def solve(self, A, target):
        mid = 0
        start = 0
        end = len(A) - 1

        while(start <= end):
            mid = start + (end-start)//2

            if (A[mid] < target) or (A[mid] == target and start < (len(A)-1) and  A[start+1] == target):
                start = mid+1
            elif A[mid] >  target:
                end = mid-1
            else:
                return mid
        return -1

sol = Solution()
A = [1,2,2,2,2,2,2,3,4,5]
target = 2
output = sol.solve(A,target)
print(output)
