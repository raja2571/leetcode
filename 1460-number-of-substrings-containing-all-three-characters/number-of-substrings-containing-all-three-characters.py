class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = {"a":0,"b":0,"c":0}
        start = 0
        ans =0
        for end in range(len(s)):
            freq[s[end]] += 1
            while freq["a"] > 0 and freq["b"]>0 and freq["c"]>0:
                ans+=(len(s)-end)
                freq[s[start]] -= 1
                start = start + 1
        return ans
        