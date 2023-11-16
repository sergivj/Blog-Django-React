from authentification.domain.models.user_model import User
from authentification.domain.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_users(self):
        return self.user_repository.get_all()

    def get_user_by_email(self, user_email: str):
        self.user_repository.get_by_email(user_email)

    def get_user_by_username(self, user_username: str):
        return self.user_repository.get_by_username(user_username)

    def get_user_by_id(self, user_id: int):
        self.user_repository.get_by_id(user_id)

    def create_user(self, user: User):
        self.user_repository.create(user)

    def update_user(self, user: User):
        self.user_repository.update(user)

    def delete_user(self, user_id: int):
        self.user_repository.delete(user_id)
