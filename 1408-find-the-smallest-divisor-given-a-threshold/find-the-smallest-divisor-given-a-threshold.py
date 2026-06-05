class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left < right:
            mid = (left+right) // 2
            total = 0
            for i in nums:
                total +=  (i + mid -1) // mid
            if total <= threshold:
                right = mid
            else:
                left = mid + 1
        return left

        