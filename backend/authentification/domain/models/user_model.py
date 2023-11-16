from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser, models.Model):
    username = models.CharField(max_length=50, unique=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=500)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True, auto_now=True)

    def create_new_user(self, username, name, lastname, email, password):

        user = User(
            username=username,
            first_name=name,
            last_name=lastname,
            email=email,
            password=password,

            is_admin=False,
            is_active=True,
            is_staff=False,
            is_superuser=False,

            last_login=timezone.now(),
            date_joined=timezone.now()
        )
        user.set_password(password)
        user.save()
        return user
