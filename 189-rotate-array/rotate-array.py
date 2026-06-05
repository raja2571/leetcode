class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k = k % n
        def reverse_method(arr,l,r):
            while l < r:
                arr[l] , arr[r] = arr[r], arr[l]
                l+=1
                r-=1
        reverse_method(nums,0,n-1)
        reverse_method(nums,0,k-1)
        reverse_method(nums,k,n-1)
        return nums


        