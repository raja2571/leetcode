class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for end in range(len(nums)):
            if nums[end] != 0:
                nums[end] , nums[j] = nums[j] , nums[end]
                j = j+1
        return nums