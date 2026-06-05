class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        bucket =[[] for _ in range(len(s) + 1)]
        for char in freq:
            count = freq[char]
            bucket[count].append(char)
        ans = ""
        for i in range(len(s),0,-1):
            for cha in bucket[i]:
                ans+=cha * i
        return ans


          