import heapq as hq

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for tweet in self.tweets[userId]:
            hq.heappush(heap, tweet)
            if len(heap) > 10:
                hq.heappop(heap)
        
        for followee in self.following[userId]:
            for tweet in self.tweets[followee]:
                hq.heappush(heap, tweet)
                if len(heap) > 10:
                    hq.heappop(heap)
        
        return [tweet for (_, tweet) in sorted(heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
