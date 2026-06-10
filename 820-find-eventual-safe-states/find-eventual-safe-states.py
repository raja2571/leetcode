from typing import List
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        rev = [[] for _ in range(n)]
        indegree = [0] * n

        for u in range(n):
            indegree[u] = len(graph[u])

            for v in graph[u]:
                rev[v].append(u)

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        safe = []

        while q:
            node = q.popleft()
            safe.append(node)

            for prev in rev[node]:
                indegree[prev] -= 1

                if indegree[prev] == 0:
                    q.append(prev)

        return sorted(safe)