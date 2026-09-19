class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        n = len(s)
        wordSet = set(wordDict)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):

            if dp[i] == False:
                continue

            for word in wordSet:

                end = i + len(word)

                if end <= n and s[i:end] == word:
                    dp[end] = True

        return dp[n]