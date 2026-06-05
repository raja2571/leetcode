class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        moves = 0
        for chr in s:
            if chr == "(":
                count +=1
            else:
                if count > 0:
                    count -=1
                else:
                    moves += 1
        return moves + count 
        