class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        curr_sum = sum(cardPoints[:k])
        max_sum = curr_sum
        for i in range(1,k+1):
            curr_sum -= cardPoints[k-i]
            curr_sum += cardPoints[n-i]
            max_sum = max(max_sum,curr_sum)
        return max_sum
        