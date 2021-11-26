# time O(n)
# space O(1)

class Solution:
    def tribonacci(self, n: int) -> int:
        f1, f2, f3 = 0, 1, 1

        if n < 3:
            return 1 if n else 0

        for _ in range(2, n):
            fNew = f1 + f2 + f3
            f1, f2, f3 = f2, f3, fNew

        return fNew
