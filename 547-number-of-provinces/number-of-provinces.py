class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visted = [False]*n
        province = 0
        def dfs(city):
            visted[city] = True
            for neg in range(n):
                if isConnected[city][neg]==1 and  not visted[neg]:
                    dfs(neg)
        for city in range(n):
            if not visted[city]:
                province +=1
                dfs(city)
        return province




        
        