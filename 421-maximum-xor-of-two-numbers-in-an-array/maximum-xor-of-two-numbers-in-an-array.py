class Solution:
    def findMaximumXOR(self, nums):
        ans = 0
        mask = 0

        for i in range(31, -1, -1):
            mask |= (1 << i)
            s = set()

            for num in nums:
                s.add(num & mask)

            temp = ans | (1 << i)

            for p in s:
                if temp ^ p in s:
                    ans = temp
                    break

        return ans
        