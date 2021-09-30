class Solution:
    def solve(self, A, target):
        sum = A[0]
        start = 0
        end = 0
        lenA = len(A)

        while(start < lenA):
            if(start > end):
                end = start
                sum = A[start]
            elif sum < target:
                if end== lenA-1:
                    break
                end += 1
                sum += A[end]      
            elif sum > target:
                sum -= A[start]
                start +=1          
            else:
                return [start, end]
        return []

sol = Solution()
A = [5,24,3,1,7,6,2,3]
target = 14
output = sol.solve(A, target)
print(output)
