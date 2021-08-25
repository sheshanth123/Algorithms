"""
Problem Description

Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.



Input Format
First and only argument is an integer array A.



Output Format
Return 1 if any such integer p is found else return -1.



Example Input
Input 1:

 A = [3, 2, 1, 3]
Input 2:

 A = [1, 1, 3, 3]


Example Output
Output 1:

 1
Output 2:

 -1


Example Explanation
Explanation 1:

 For integer 2, there are 2 greater elements in the array. So, return 1.
Explanation 2:

 There is no such integer exists.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        inputSize = len(A)
        A.sort()
        for i in range(1, inputSize):
            #since we can have duplicates, instead of checking the current index, check the previous index
            if (A[i-1] != A[i]) and (A[i-1] == (inputSize - i)):
                return 1 
        #since in the for loop, our last index would never be handled, we need to check for the last index
        if A[inputSize-1] == 0:
            return 1
        return -1
