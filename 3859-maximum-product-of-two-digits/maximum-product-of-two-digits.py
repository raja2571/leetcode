class Solution:
    def maxProduct(self, n: int) -> int:
        first = 0
        second = 0

        while n > 0:
            d = n % 10

            if d >= first:
                second = first
                first = d
            elif d > second:
                second = d

            n //= 10

        return first * second