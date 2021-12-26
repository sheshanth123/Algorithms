# time O(n)
# space O(n)

class Solution:
    # @param A : integer
    # @return an integer
    def getBinRep(self, A):
        binRep  = []

        while A > 0:
            binRep.append(A%2)

            A = A//2
        return binRep
    
    def solve(self, A):
        binRep = self.getBinRep(A)

        finalAnswer = 0

        for currIndex in range(len(binRep)):
            if binRep[currIndex]:
                finalAnswer += 5 ** (currIndex+1)
        return finalAnswer
