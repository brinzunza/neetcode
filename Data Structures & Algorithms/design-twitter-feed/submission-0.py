class Twitter:

    def __init__(self):
        self.posts = []
        self.following = {}


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        possible = self.posts.copy()
        following = self.following.get(userId, [])
        while len(feed) < 10:
            if not possible:
                break
            post = possible.pop()
            if post[0] in following or post[0] == userId:
                feed.append(post[1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        followees = self.following.get(followerId, [])
        if followeeId not in followees:
            followees.append(followeeId)
            self.following[followerId] = followees

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followees = self.following.get(followerId, [])
        if followeeId in followees:
            followees.remove(followeeId)
            self.following[followerId] = followees