class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zerocount = 0
        max_lenght = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zerocount += 1
            if zerocount >  k:
                if nums[left] == 0:
                    zerocount -= 1
                left =left + 1
            max_lenght = max(max_lenght,right - left + 1)
        return max_lenght 
        
        