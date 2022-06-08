from urllib import request

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    mobile = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=255, default='')
    is_viewer = models.BooleanField(default=True)

    # def save(self, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         hashed_password = make_password(self.password)
    #         self.password = hashed_password
    #         # if not hashed_password == self.password:
    #         #     self.password = hashed_password
    #
    #     super().save()



