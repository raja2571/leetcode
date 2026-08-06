class Solution:
    def reverseVowels(self, s: str) -> str:
        l=list(s)
        left = 0
        right = len(s)-1
        while left < right:
            while left < right and l[left] not in "aeiouAEIOU":
                left+=1
            while left < right and l[right] not in "aeiouAEIOU":
                right-=1
            l[left],l[right] = l[right],l[left]
            left+=1
            right-=1
        return "".join(l)
            

        