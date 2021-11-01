"""
Given an array of integers A and an integer B. Find and return the maximum value of | s1 - s2 |

where s1 = sum of any subset of size B, s2 = sum of elements of A - sum of elemets of s1

Note |x| denotes the absolute value of x.


Input Format

The arguments given are the integer array A and integer B.
Output Format

Return the maximum value of | s1 - s2 |.
Constraints

1 <= B < length of the array <= 100000
1 <= A[i] <= 10^5 
For Example

Input 1:
    A = [1, 2, 3, 4, 5]
    B = 2
Output 1:
    9

Input 2:
    A = [5, 17, 100, 11]
    B = 3
Output 2:
    123
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        A.sort()

        lenA = len(A)

        sumA = 0

        for elem in A:
            sumA += elem

        s1 = 0

        for elemIndex in range(0, B):
            s1 += A[elemIndex]
        
        s2 = sumA - s1

        max1 = abs(s1-s2)

        s1=0

        for elemIndex in range(lenA-1,( lenA - B)-1, -1):
            s1 += A[elemIndex]
        
        s2 = sumA - s1

        max2 = abs(s1-s2)

        return max(max1, max2)
