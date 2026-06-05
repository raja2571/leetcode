class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
        def can_make(days):
            b = 0
            f = 0
            for i in bloomDay:
                if i <= days:
                    f +=1
                    if f == k:
                        b +=1
                        f = 0
                else:
                    f =0
            return b >= m
        left = 1
        right = max(bloomDay)
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if can_make(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
        