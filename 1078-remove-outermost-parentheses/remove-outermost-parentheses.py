class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        count = 0
        for chr in s:
            if chr == "(":
                if count > 0:
                    ans.append(chr)
                count += 1
            else:
                count -=1
                if count > 0:
                    ans.append(chr)
        return "".join(ans)
                    