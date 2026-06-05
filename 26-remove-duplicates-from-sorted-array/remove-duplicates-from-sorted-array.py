class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        for i in range(len(nums)):
            if nums[i] != nums[start]:
                start += 1
                nums[start] = nums[i]
        return start+1

        
        