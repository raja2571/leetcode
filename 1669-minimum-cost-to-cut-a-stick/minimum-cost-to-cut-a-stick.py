class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]

        m = len(cuts)
        dp = [[0] * m for _ in range(m)]

        for length in range(2, m):
            for i in range(m - length):
                j = i + length
                dp[i][j] = float('inf')

                for k in range(i + 1, j):
                    dp[i][j] = min(
                        dp[i][j],
                        cuts[j] - cuts[i] + dp[i][k] + dp[k][j]
                    )

                if dp[i][j] == float('inf'):
                    dp[i][j] = 0

        return dp[0][m - 1]