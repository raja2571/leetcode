class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            day_count = 1
            total = 0
            for i in weights:
                if total + i > capacity:
                    day_count +=1
                    total = 0
                total +=i
            return day_count <= days
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid
            else:
                left =mid + 1
        return left
        