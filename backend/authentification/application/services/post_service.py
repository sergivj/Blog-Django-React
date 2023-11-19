from authentification.domain.models.post_model import Post
from authentification.domain.repositories.post_repository import PostRepository


class PostService:

    def __init__(self):
        self.post_repository = PostRepository()

    def get_posts(self):
        return self.post_repository.get_posts()

    def create_post(self, post: Post):
        return self.post_repository.create_post(post)

    def delete_post(self, post_id: int):
        return self.post_repository.delete_post(post_id)
