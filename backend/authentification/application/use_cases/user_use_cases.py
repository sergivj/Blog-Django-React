from typing import List
from backend.authentification.domain.models import User
from backend.authentification.application.services import UserService


class UserUseCases:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

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
