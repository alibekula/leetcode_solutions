# Last updated: 12.09.2025, 22:29:29
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.tw = defaultdict(list)
        self.ts = 0
        self.fw = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        item = [-self.ts, tweetId]
        self.ts += 1
        self.tw[userId].append(item)

    def getNewsFeed(self, userId: int) -> List[int]:
        users = {userId} | self.fw[userId]
        heap = []

        for u in users:
            for ts, tw in self.tw[u][-10:]:
                heapq.heappush(heap, [ts, tw])
        
        ans = []

        for i in range(10):
            if heap:
                _, tw = heapq.heappop(heap)
                ans.append(tw)
        
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.fw[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.fw[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)