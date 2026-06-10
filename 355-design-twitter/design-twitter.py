from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        heap = []

        self.following[userId].add(userId)

        for user in self.following[userId]:
            tweets = self.tweets[user]

            if tweets:
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]
                heapq.heappush(heap, (-time, tweetId, user, idx - 1))

        ans = []

        while heap and len(ans) < 10:
            time, tweetId, user, idx = heapq.heappop(heap)
            ans.append(tweetId)

            if idx >= 0:
                t, tid = self.tweets[user][idx]
                heapq.heappush(heap, (-t, tid, user, idx - 1))

        return ans

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)