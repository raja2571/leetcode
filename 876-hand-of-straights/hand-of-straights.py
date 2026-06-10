from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)

        for num in sorted(count):
            freq = count[num]

            if freq > 0:
                for i in range(num, num + groupSize):
                    if count[i] < freq:
                        return False
                    count[i] -= freq

        return True
        