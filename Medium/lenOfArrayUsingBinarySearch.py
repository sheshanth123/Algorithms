class Solution:

    def getLenOfArr(self, A):
        high = 1

        while True:
            try:
                A[high]
                high *= 2
            except IndexError as e:
                break
        start = high//2
        end = high
        lenArr = start

        while(start <= end):
            mid = start + (end-start)//2
            try:
                A[mid]
                lenArr = max(mid, lenArr)
                start = mid+1
            except:
                end = mid-1
        return lenArr+1

    def solve(self, A):
        return self.getLenOfArr(A)
                 
sol = Solution()
A = [1,2,3]
output = sol.solve(A)
print(output)
