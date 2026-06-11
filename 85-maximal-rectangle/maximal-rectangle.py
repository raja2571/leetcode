class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        n = len(matrix[0])
        heights = [0] * n

        def largestRectangleArea(heights):
            stack = []
            max_area = 0

            for i in range(len(heights) + 1):
                curr = 0 if i == len(heights) else heights[i]

                while stack and heights[stack[-1]] > curr:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)

                stack.append(i)

            return max_area

        ans = 0

        for row in matrix:
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0

            ans = max(ans, largestRectangleArea(heights))

        return ans