"""
Arithmetic Progression?
Problem Description

Given an integer array A of size N. Return 1 if the array can be rearranged to form an arithmetic progression, otherwise, return 0.

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.



Problem Constraints
2 <= N <= 105

-109 <= A[i] <= 109



Input Format
First and only argument is an integer array A of size N.



Output Format
Return 1 if the array can be rearranged to form an arithmetic progression, otherwise, return 0



Example Input
Input 1:

 A = [3, 5, 1]
Input 2:

 A = [2, 4, 1]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
Explanation 2:

 There is no way to reorder the elements to obtain an arithmetic progression.
"""
# O(3N) ~ O(N) solution
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        lenA = len(A)
        
        if lenA < 2:
            return 1
        
        firstMin = A[0]
        secondMin = A[1]
        #get first min and secon min
        for i in range(lenA):
            if A[i] < firstMin:
                secondMin = firstMin
                firstMin = A[i]
            #it might also be possible that firstMin has min but value of secondMin 
            #might be greater than the curr element
            elif A[i] < secondMin:
                secondMin = A[i]
                
        #load all the array elemnts in hashmap         
        hasmMap = {}
        for i in range(lenA):
            hasmMap[A[i]] = i
        
        diff = secondMin - firstMin
        
        #get the diff of elements and check if present in hashmap
        for i in A:
            # it is quite possible that the currElement can be the min and would
            # not be found in the hashMap
            if i is not firstMin:
                if hasmMap.get(i-diff) is None:
                    return 0

        return 1
