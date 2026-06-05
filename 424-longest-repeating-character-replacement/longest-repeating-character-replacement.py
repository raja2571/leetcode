class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_len = 0
        max_fre = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) + 1
            max_fre = max(max_fre, count[s[right]]) 
            while (right-left+1) - max_fre > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len,right - left + 1)
        return max_len 
