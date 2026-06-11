class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            cur_max = 0
            best = 0

            for j in range(i, min(n, i + k)):
                cur_max = max(cur_max, arr[j])
                best = max(best, cur_max * (j - i + 1) + dp[j + 1])

            dp[i] = best

        return dp[0]