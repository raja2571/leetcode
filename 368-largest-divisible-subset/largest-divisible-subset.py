class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        dp = [1] * n
        parent = list(range(n))

        max_len = 1
        last_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                last_idx = i

        res = []
        while parent[last_idx] != last_idx:
            res.append(nums[last_idx])
            last_idx = parent[last_idx]

        res.append(nums[last_idx])

        return res[::-1]