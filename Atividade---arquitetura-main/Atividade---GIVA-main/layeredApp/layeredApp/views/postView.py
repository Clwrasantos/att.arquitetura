from domain.post import Post
from workers.postWorker import PostWorker

class PostView:
    postWorker: PostWorker

    def __init__(self):
        self.postWorker = PostWorker()

    def createPost(self):
        print("Creating a new post")
        message = input("Insert the post message: ")
        user_id = int(input("Insert the author user ID: "))

        post = Post(message=message, user_id=user_id)
        self.postWorker.add(post)
        print("Post created successfully!")

    def listPosts(self):
        posts = self.postWorker.getAll()
        print("Listing posts:")
        for post in posts:
            print(f"Post ID: {post.id}, Author ID: {post.user_id}, Message: {post.message}")
