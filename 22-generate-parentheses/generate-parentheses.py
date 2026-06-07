class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def gp(s,o_p,c_p):
            if len(s) == 2*n:
                ans.append(s)
                return
            if o_p < n:
                gp(s+"(",o_p+1,c_p)
            if c_p < o_p:
                gp(s+")",o_p,c_p+1)
        gp("",0,0)
        return ans
        