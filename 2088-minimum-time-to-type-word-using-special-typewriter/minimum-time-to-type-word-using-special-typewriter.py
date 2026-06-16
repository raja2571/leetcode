class Solution:
    def minTimeToType(self, word: str) -> int:
        curr = 'a'
        ans = 0

        for ch in word:
            diff = abs(ord(ch) - ord(curr))
            ans += min(diff, 26 - diff) + 1
            curr = ch

        return ans