class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        frist = strs[0]
        last = strs[-1]
        i =0
        while i < len(frist) and frist[i] == last[i]:
            i+=1
        return frist[:i]

        