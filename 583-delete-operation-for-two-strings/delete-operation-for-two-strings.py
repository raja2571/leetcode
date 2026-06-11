class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def lcs(i, j):
            if i == len(word1) or j == len(word2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = 1 + lcs(i + 1, j + 1)
            else:
                memo[(i, j)] = max(
                    lcs(i + 1, j),
                    lcs(i, j + 1)
                )

            return memo[(i, j)]

        common = lcs(0, 0)

        return len(word1) + len(word2) - 2 * common
        