from authentification.domain.models.post_model import Post
from authentification.domain.models.user_model import User


class PostRepository:
    def get_posts(self):
        return Post.objects.all().order_by('-date_posted')

    def get_post(self, post_id: int):
        raise NotImplementedError

    def create_post(self, post: Post):
        Post.objects.create(title=post['title'], content=post['content'], author=User(id=post['author']['id']))

    def update_post(self, post: Post):
        raise NotImplementedError

    def delete_post(self, post_id: int):
        Post.objects.get(id=post_id).delete()
