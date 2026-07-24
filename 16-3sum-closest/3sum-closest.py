class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if abs(target - s) < abs(target - closest):
                    closest = s

                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return target

        return closest