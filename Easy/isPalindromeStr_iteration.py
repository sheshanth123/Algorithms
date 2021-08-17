class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        lenStr = len(A)
        
        #check start and first characters itertively and we just need to go till the middle
        for i in range(lenStr//2):
            if A[i] == A[lenStr-i-1]:
                continue
            #if the first and last character are not eual return 0
            return 0
        #at this point we are sure that the string is palindrome hence return 1
        return 1
