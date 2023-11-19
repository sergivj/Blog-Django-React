from typing import List

from authentification.application.services.user_service import UserService
from authentification.domain.models.user_model import User


class UserUseCases:
    def __init__(self):
        self.user_service = UserService()

    def create_user(self, user: User) -> User:
        return self.user_service.create_user(user)

    def get_user_by_id(self, user_id: int) -> User:
        return self.user_service.get_user_by_id(user_id)

    def get_user_by_email(self, email: str) -> User:
        return self.user_service.get_user_by_email(email)

    def get_user_by_username(self, username: str) -> User:
        return self.user_service.get_user_by_username(username)

    def get_all_users(self) -> List[User]:
        return self.user_service.get_users()

    def update_user(self, user: User) -> User:
        return self.user_service.update_user(user)

    def delete_user(self, user_id: int) -> None:
        self.user_service.delete_user(user_id)
