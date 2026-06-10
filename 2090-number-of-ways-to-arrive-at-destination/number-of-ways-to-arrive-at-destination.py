from typing import List
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7

        graph = [[] for _ in range(n)]

        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        dist = [float('inf')] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for nei, wt in graph[node]:
                nd = d + wt

                if nd < dist[nei]:
                    dist[nei] = nd
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (nd, nei))

                elif nd == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % mod

        return ways[n - 1]