"""
Bulbs
Problem Description

N light bulbs are connected by a wire.

Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb.

Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.

You can press the same switch multiple times.

Note: 0 represents the bulb is off and 1 represents the bulb is on.



Problem Constraints
1 <= N <= 5*105
0 <= A[i] <= 1



Input Format
The first and the only argument contains an integer array A, of size N.



Output Format
Return an integer representing the minimum number of switches required.



Example Input
Input 1:

 A = [0, 1, 0, 1]
Input 2:

 A = [1, 1, 1, 1]


Example Output
Output 1:

 4
Output 2:

 0


Example Explanation
Explanation 1:

 press switch 0 : [1 0 1 0]
 press switch 1 : [1 1 0 1]
 press switch 2 : [1 1 1 0]
 press switch 3 : [1 1 1 1]
Explanation 2:

 There is no need to turn any switches as all the bulbs are already on.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):

        countSwitch = 0

        for elem in A:
            # if elem is 1 and the countSwitch is even then continue
            if elem and (countSwitch % 2 == 0):
                continue
            # if countSwitch is odd then increase count
            elif countSwitch % 2 == 1:
                # if elem was 0 after switch it might be 1 now
                if elem == 0:
                    continue
                # the elem might be 1 and might be 0, so increase the count
                countSwitch += 1
            # here the elem is 0 and countSwitch is even
            else:
                countSwitch += 1
        return countSwitch
