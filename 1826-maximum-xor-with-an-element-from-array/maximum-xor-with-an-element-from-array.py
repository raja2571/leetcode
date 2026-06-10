from typing import List

class TrieNode:
    def __init__(self):
        self.child = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root

        for i in range(31, -1, -1):
            bit = (num >> i) & 1

            if bit not in node.child:
                node.child[bit] = TrieNode()

            node = node.child[bit]

    def getMaxXor(self, num):
        node = self.root
        ans = 0

        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            want = 1 - bit

            if want in node.child:
                ans |= (1 << i)
                node = node.child[want]
            else:
                node = node.child[bit]

        return ans


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()

        q = []
        for i, (x, m) in enumerate(queries):
            q.append((m, x, i))

        q.sort()

        trie = Trie()
        ans = [-1] * len(queries)

        j = 0

        for m, x, idx in q:
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1

            if j > 0:
                ans[idx] = trie.getMaxXor(x)

        return ans
        