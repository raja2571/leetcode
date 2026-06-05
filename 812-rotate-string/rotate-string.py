class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            ro=s[i:]+s[:i]
            if ro==goal:
                return True
        return False
        