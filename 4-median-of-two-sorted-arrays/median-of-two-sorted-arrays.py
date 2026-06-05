class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        x = len(nums1)
        y = len(nums2)
        left = 0
        right = x
        while left <= right:
            partX = (left + right) // 2
            partY = (x+y+1)//2 - partX
            maxleftX = float("-inf") if partX == 0 else nums1[partX - 1]
            minRightX = float("inf") if partX == x else nums1[partX]
            maxleftY = float("-inf") if partY == 0 else nums2[partY-1]
            minRightY = float("inf") if partY == y else nums2[partY]
            if maxleftX <= minRightY and maxleftY <= minRightX:
                if (x + y) % 2 == 1:
                    return float(max(maxleftX, maxleftY))
                return ( max(maxleftX, maxleftY) + min(minRightX,minRightY)) / 2
            elif maxleftX > minRightY:
                right = partX  - 1
            else:
                left = partX + 1        