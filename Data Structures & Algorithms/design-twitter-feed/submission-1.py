class Twitter:
    """
    post: {userId: ((-1, tweetid), (-2, tweetid)
    follows: {userId: (userId, )} -> (hash = {key, set()})
    
    
    getNewsFeed :
        1. check following 
        2 for id in follows[userid]:
            return post tweetids from last to first (sort in decreasing order using max heap)

    """
    def __init__(self):
        self.posts = defaultdict(list)
        self.followList = defaultdict(set)
        self.count = 0


    def postTweet(self, userId: int, tweetId: int):
        self.posts[userId].append((self.count, tweetId))
        self.count += 1
       
    def getNewsFeed(self, userId):
        temp = list(self.posts[userId])
        for followeeId in self.followList[userId]:
            temp.extend(self.posts[followeeId])
        out = heapq.nlargest(10, temp)
        return [val for _, val in out]
    
    def follow(self, followerId, followeeId):
        self.followList[followerId].add(followeeId)
    
    def unfollow(self, followerId, followeeId):
        self.followList[followerId].discard(followeeId) 
        



            



