class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def dfs(index,path,total):
            if len(path) == k:
                if total == n:
                    ans.append(path[:])
                return
            if total > n:
                return
            for i in range(index,10):
                path.append(i)
                dfs(i+1,path,total+i)
                path.pop()


        dfs(1,[],0)
        return ans