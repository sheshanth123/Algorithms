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

    def solve(self, A, target):
        lenArr =  self.getLenOfArr(A)

        start = 0
        end = lenArr

        while(start <= end):
            mid = start + (end-start) //2

            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid +1
            else:
                end = mid-1
        return -1
           
sol = Solution()
target = 1
A = [1,2,3,4,5,6,7,8,9]
output = sol.solve(A, target)
print(output)
