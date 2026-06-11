class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        is_pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        dp = [0] * (n + 1)
        dp[n] = -1

        for i in range(n - 1, -1, -1):
            dp[i] = float('inf')
            for j in range(i, n):
                if is_pal[i][j]:
                    dp[i] = min(dp[i], 1 + dp[j + 1])

        return dp[0]