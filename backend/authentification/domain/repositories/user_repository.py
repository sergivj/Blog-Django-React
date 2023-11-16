from typing import Optional, List
from authentification.domain.models.user_model import User


class UserRepository:
    def create(self, user: User) -> User:
        raise NotImplementedError

    def get_by_email(self, email: str) -> Optional[User]:
        raise NotImplementedError

    def get_by_id(self, id: int) -> Optional[User]:
        return User.objects.get(id=id)

    def get_by_username(self, username: str) -> Optional[User]:
        return User.objects.get(username=username)

    def get_all(self) -> List[User]:
        return User.objects.all()

    def update(self, user: User) -> User:
        raise NotImplementedError

    def delete(self, user: User) -> User:
        raise NotImplementedError
