class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uni_char = set()
        start = 0
        max_lenght = 0
        for end in range(len(s)):
            while s[end] in uni_char:
                uni_char.remove(s[start])
                start += 1

            uni_char.add(s[end])
            lenght = end - start + 1
            max_lenght = max(max_lenght,lenght)
        return max_lenght
    
        