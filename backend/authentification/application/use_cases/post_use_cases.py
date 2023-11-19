from authentification.application.services.post_service import PostService
from authentification.domain.models.post_model import Post


class PostUseCases:
    def __init__(self):
        self.post_service = PostService()

    def get_posts(self):
        return self.post_service.get_posts()

    def get_post(self, post_id: int):
        self.post_service.get_post(post_id)

    def create_post(self, post: Post):
        self.post_service.create_post(post)

    def update_post(self, post: Post):
        self.post_service.update_post(post)

    def delete_post(self, post_id: int):
        self.post_service.delete_post(post_id)
        