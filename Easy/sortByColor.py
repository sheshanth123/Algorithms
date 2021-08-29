"""
Sort by Color
Problem Description

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: Using library sort function is not allowed.



Problem Constraints
1 <= N <= 1000000
0 <= A[i] <= 2


Input Format
First and only argument of input contains an integer array A.


Output Format
Return an integer array in asked order


Example Input
Input 1 :
    A = [0 1 2 0 1 2]
Input 2:

    A = [0]


Example Output
Output 1:
    [0 0 1 1 2 2]
Output 2:

    [0]


Example Explanation
Explanation 1:
    [0 0 1 1 2 2] is the required order.
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        # Count the number 0,1,2
        countZero = 0
        countOne = 0
        countTwo = 0
        for currElem in A:
            #if the element exists in the array then increase the count
            if currElem == 0:
                countZero += 1
            elif currElem == 1:
                countOne += 1
            else:
                countTwo += 1
        # replace the original array with the 0, 1 ,2 based on count
        for currIndex in range(len(A)):
            if countZero > 0:
                A[currIndex] = 0
                countZero -= 1
            elif countOne > 0:
                A[currIndex] = 1
                countOne -= 1
            elif countTwo > 0:
                A[currIndex] = 2
                countTwo -= 1
        return A
