from authentification.domain.models.post_model import Post
from authentification.domain.repositories.post_repository import PostRepository


class PostService:

    def __init__(self):
        self.post_repository = PostRepository()

    def get_posts(self):
        return self.post_repository.get_posts()

    def get_post(self, post_id: int):
        self.post_repository.get_post(post_id)

    def create_post(self, post: Post):
        return self.post_repository.create_post(post)

    def update_post(self, post: Post):
        self.post_repository.update_post(post)

    def delete_post(self, post_id: int):
        return self.post_repository.delete_post(post_id)
