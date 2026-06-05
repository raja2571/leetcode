class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        end = 0
        max_count = 0
        for i in range(len(nums)-1):
            max_count = max(max_count,i + nums[i])
            if i == end:
                jump +=1
                end = max_count
        return jump 
        