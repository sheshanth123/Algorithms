The Fibonacci sequence goes like this: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number can be found by adding up the two numbers before it, and the first two numbers are always 1.

Write a function that takes an integer n and returns the nth Fibonacci number in the sequence.

Note: n will be less than or equal to 30.
```python
class Solution:
    def solve(self, n):
        # Write your code here
        a, b =1,1
        
        for _ in range(2,n):
            a,b = b, a+b
        return b

Let F be the Fibonacci sequence. After the t-th step, lets maintain a=F_{t}, b=F_{t + 1}. Then after the (n - 1)-th step, we will have b = F_n as desired.
```
