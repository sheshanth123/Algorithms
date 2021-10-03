class Solution:

    def solve(self, A, target):

        start, end = 0, len(A)-1
        result = end
        while(start <= end):
            mid = start + (end-start)//2

            if A[mid] == target:
                return A[mid]
            elif A[mid] < target:
                start = mid+1
            else:
                end = mid -1 
            
            if abs(target - A[mid]) < abs(target - result):
                result = A[mid] 
            

        return result
            
sol = Solution()
A = [10, 23, 30, 40, 50, 60, 70]
output = sol.solve(A, 73)
print(output)
