class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        # write a helper function to get the digits
        def sumSquares(n):
            res = 0
            while n:
                digit = n % 10
                digit = digit ** 2
                res += digit
                n = n // 10
            return res

        while n not in seen:
            seen.add(n)
            n = sumSquares(n)
            if n == 1:
                return True
        return False