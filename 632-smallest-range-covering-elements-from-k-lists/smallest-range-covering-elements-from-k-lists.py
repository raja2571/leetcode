import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        mx = float('-inf')

        for i, lst in enumerate(nums):
            heap.append((lst[0], i, 0))
            mx = max(mx, lst[0])

        heapq.heapify(heap)

        start, end = -10**5, 10**5

        while True:
            mn, row, col = heapq.heappop(heap)

            if mx - mn < end - start:
                start, end = mn, mx

            if col + 1 == len(nums[row]):
                break

            nxt = nums[row][col + 1]
            mx = max(mx, nxt)
            heapq.heappush(heap, (nxt, row, col + 1))

        return [start, end]