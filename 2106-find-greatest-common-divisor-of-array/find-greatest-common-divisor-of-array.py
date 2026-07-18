class Solution:
    def findGCD(self, nums):
        smallest = min(nums)
        largest = max(nums)

        while largest != 0:
            smallest, largest = largest, smallest % largest

        return smallest