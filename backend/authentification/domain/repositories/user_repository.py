from typing import Optional, List

from django.utils import timezone

from authentification.domain.models.user_model import User


class UserRepository:
    def create(self, user: User) -> User:
        if self.get_by_email(user['email']) or self.get_by_username(user['username']):
            raise ValueError('User already exists')

        new_user = User(
            username=user['username'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            email=user['email'],
            password=user['password'],

            is_admin=False,
            is_active=True,
            is_staff=False,
            is_superuser=False,

            last_login=timezone.now(),
            date_joined=timezone.now()
        )
        new_user.set_password(user['password'])
        new_user.save()
        return new_user

    def get_by_email(self, email: str) -> Optional[User]:
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def get_by_id(self, id: int) -> Optional[User]:
        return User.objects.get(id=id)

    def get_by_username(self, username: str) -> Optional[User]:
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def get_all(self) -> List[User]:
        return User.objects.all()

