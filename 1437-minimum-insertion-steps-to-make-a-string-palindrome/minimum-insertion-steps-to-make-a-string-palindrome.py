class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        memo ={}
        def dfs(i,j):
            if i>=j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i] == s[j]:
                memo[(i,j)] = dfs(i+1,j-1)
            else:
                memo[(i,j)] = 1+ min(dfs(i+1,j),dfs(i,j-1))
            return memo[(i,j)]
        return dfs(0,n-1)
        