class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def pattern(string):
            p = []
            f_s = {}
            index = 0
            for chr in string:
                if chr not in f_s:
                    f_s[chr] = index
                    index += 1
                p.append(f_s[chr])
            return p
        return pattern(s) == pattern(t)
        